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

Using SSH:

```sh
USE_SSH=true yarn deploy
```

Not using SSH:

```sh
GIT_USER=<Your GitHub username> yarn deploy
```

If you are using GitHub pages for hosting, this command is a convenient way to build the website and push to the `gh-pages` branch.
