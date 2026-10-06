#!/usr/bin/env python3
"""
Embed the knowledge base docs into an embeddings.json index served with the site.
"""

import argparse
import glob
import json
import os
import re
import urllib.error
import urllib.parse
import urllib.request

from langchain_text_splitters import MarkdownTextSplitter

MODEL_ID = "intfloat/multilingual-e5-large"
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 100
BATCH_SIZE = 100
# e5 models expect "passage: " on documents and "query: " on search queries
PASSAGE_PREFIX = "passage: "

FRONT_MATTER = re.compile(r"^---\n(.*?)\n---\n", re.S)
IMPORT = re.compile(r"^import\s+(\w+)\s+from\s+['\"](.+?)['\"];?\s*$", re.M)
# Fenced blocks and inline code are literal text in MDX, so imports/components inside them are left alone
CODE = re.compile(r"(^(`{3,}|~{3,}).*?^\2[ \t]*$|`[^`\n]+`)", re.M | re.S)
# Only the page content between these markers is embedded; files without markers (e.g. partials) are embedded whole
EMBED = re.compile(r"<!--\s*embed:start\s*-->(.*?)<!--\s*embed:end\s*-->", re.S)


def post(url, data, headers):
    request = urllib.request.Request(url, data=data, headers=headers, method="POST")
    with urllib.request.urlopen(request) as response:
        return json.load(response)


def iam_token(api_key):
    body = urllib.parse.urlencode(
        {"grant_type": "urn:ibm:params:oauth:grant-type:apikey", "apikey": api_key}
    ).encode()
    return post(
        "https://iam.cloud.ibm.com/identity/token",
        body,
        {"Content-Type": "application/x-www-form-urlencoded"},
    )["access_token"]


def embed(texts, embedding_url, token, project_id):
    embeddings = []
    for i in range(0, len(texts), BATCH_SIZE):
        body = json.dumps(
            {
                "model_id": MODEL_ID,
                "project_id": project_id,
                "inputs": [PASSAGE_PREFIX + text for text in texts[i : i + BATCH_SIZE]],
                "parameters": {"truncate_input_tokens": 512},
            }
        ).encode()
        response = post(
            embedding_url,
            body,
            {"Authorization": f"Bearer {token}", "Content-Type": "application/json"},
        )
        embeddings.extend(result["embedding"] for result in response["results"])
    return embeddings


def render(path):
    content = open(path, encoding="utf-8").read()
    front_matter = FRONT_MATTER.match(content)
    meta = (
        dict(
            line.split(":", 1)
            for line in front_matter.group(1).splitlines()
            if ":" in line
        )
        if front_matter
        else {}
    )
    content = content[front_matter.end() :] if front_matter else content

    segments = CODE.split(content)
    # split() yields [prose, code, fence, prose, code, fence, ...]; only prose is MDX
    prose = "\n".join(segments[0::3])
    partials = {
        name: os.path.join(os.path.dirname(path), partial)
        for name, partial in IMPORT.findall(prose)
        if partial.endswith((".md", ".mdx"))
    }

    marked = EMBED.findall(content)
    if marked:
        content = "\n".join(marked)
        segments = CODE.split(content)

    def render_prose(text):
        for name, partial in partials.items():
            text = re.sub(rf"<{name}\s*/>", lambda _: render(partial)[0], text)
        text = IMPORT.sub("", text)
        text = re.sub(r"<[A-Z]\w*[^>]*/>", "", text)
        return re.sub(r"<!--.*?-->", "", text, flags=re.S)

    content = "".join(
        render_prose(segment) if i % 3 == 0 else segment if i % 3 == 1 else ""
        for i, segment in enumerate(segments)
    )

    return content.strip(), {
        key.strip(): value.strip().strip("'\"") for key, value in meta.items()
    }


def page_url(path, docs_path, base_url, meta):
    slug = meta.get("slug")
    if not slug:
        slug = "/" + os.path.splitext(os.path.relpath(path, docs_path))[0]
        # Docusaurus serves index/README docs at their folder's URL
        slug = re.sub(r"/(index|README)$", "", slug, flags=re.I) or "/"
    return base_url.rstrip("/") + urllib.parse.quote(slug)


def load_chunks(docs_path, base_url):
    splitter = MarkdownTextSplitter(chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP)
    texts, metadata = [], []

    for path in sorted(glob.glob(os.path.join(docs_path, "**/*.md*"), recursive=True)):
        if os.path.basename(path).startswith("_"):
            continue

        content, meta = render(path)
        heading = re.search(r"^#\s+(.+)$", content, re.M)
        title = meta.get("title") or (
            heading.group(1).strip() if heading else os.path.basename(path)
        )
        url = page_url(path, docs_path, base_url, meta)

        for chunk in splitter.split_text(content):
            texts.append(f"{title}\n{chunk}")
            metadata.append({"url": url, "title": title})

    return texts, metadata


def load_previous(source):
    """Return {text: embedding} from a previously published index, so unchanged chunks are not re-embedded."""
    try:
        if source.startswith(("http://", "https://")):
            with urllib.request.urlopen(source) as response:
                previous = json.load(response)
        else:
            with open(source, encoding="utf-8") as f:
                previous = json.load(f)
    except (OSError, urllib.error.URLError, ValueError) as error:
        print(f"No previous index at {source} ({error}), embedding everything")
        return {}

    if (
        previous.get("model") != MODEL_ID
        or previous.get("passage_prefix") != PASSAGE_PREFIX
    ):
        print(
            "Previous index used a different model or input format, embedding everything"
        )
        return {}
    return dict(zip(previous["texts"], previous["embeddings"]))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--docs-path", default="docs")
    parser.add_argument("--base-url", default="https://docs.labs.skills.network")
    parser.add_argument("--output", default="build/embeddings.json")
    parser.add_argument(
        "--previous",
        help="previous embeddings.json path or URL to reuse (default: <base-url>/embeddings.json)",
    )
    parser.add_argument(
        "--embedding-url",
        default="https://us-south.ml.cloud.ibm.com/ml/v1/text/embeddings?version=2023-10-25",
    )
    args = parser.parse_args()

    texts, metadata = load_chunks(args.docs_path, args.base_url)
    cache = load_previous(
        args.previous or args.base_url.rstrip("/") + "/embeddings.json"
    )

    missing = sorted({text for text in texts if text not in cache})
    if missing:
        token = iam_token(os.environ["WATSONX_AI_APIKEY"])
        cache.update(
            zip(
                missing,
                embed(
                    missing,
                    args.embedding_url,
                    token,
                    os.environ["WATSONX_AI_PROJECT_ID"],
                ),
            )
        )
    embeddings = [cache[text] for text in texts]

    os.makedirs(os.path.dirname(args.output) or ".", exist_ok=True)
    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(
            {
                "model": MODEL_ID,
                "passage_prefix": PASSAGE_PREFIX,
                "texts": texts,
                "metadata": metadata,
                "embeddings": embeddings,
            },
            f,
        )

    print(
        f"Wrote {len(texts)} chunks from {len({m['url'] for m in metadata})} pages to {args.output} "
        f"({len(missing)} embedded, {len(texts) - len(missing)} reused)"
    )


if __name__ == "__main__":
    main()
