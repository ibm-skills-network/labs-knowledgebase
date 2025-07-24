# Website

## Development

### Adding content

We use [Docusaurus](https://docusaurus.io/) within these docs.

- You can find a [general set of guides to Docusaurus here](https://docusaurus.io/docs/category/guides).
- **Docusaurus provides extra cool formatting features** on top of vanilla Markdown,
  see the [guide to these features here](https://docusaurus.io/docs/markdown-features).

### Running the server

Install deps and run the dev server locally by running:

```sh
yarn
yarn start
```

Most changes are reflected live without having to restart the server.

## Building

```sh
yarn build
```

This command generates static content into the `build` directory and can be served using any static contents hosting service.

## Deploying

- Deploying to GitHub Pages occurs automatically upon merges to `main`.
- Check the [list of all `Deploy to GitHub Pages` workflow runs](https://github.com/ibm-skills-network/labs-knowledgebase/actions/workflows/deploy.yml) to ensure your changes are successfully deployed after they're merged.
