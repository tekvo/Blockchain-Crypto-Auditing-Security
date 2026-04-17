# Blockchain, crypto, and smart contract security

Curated notes and references for **blockchain security**, **smart contract auditing**, and **due diligence** on tokens and protocols.

## Browse as a website

Documentation is built with [MkDocs](https://www.mkdocs.org/) and the [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) theme. The **landing page** is [`docs/index.md`](./docs/index.md); the **sidebar navigation** is defined in [`mkdocs.yml`](./mkdocs.yml). Each guide opens on its own page under [`docs/guides/`](./docs/guides/).

### Run locally

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
mkdocs serve
```

Then open [http://127.0.0.1:8000/](http://127.0.0.1:8000/). Click items in the nav or in the tables on the home page to move between documents.

### Publish to GitHub Pages

```bash
mkdocs gh-deploy
```

If you use the included GitHub Actions workflow, pushing to the default branch builds and deploys the site to the `gh-pages` branch.

## Repository layout

| Path | Purpose |
|------|---------|
| [`docs/`](./docs/) | Site source: landing page, guides, code-samples page |
| [`docs/guides/`](./docs/guides/) | One markdown file per topic (former `001`–`012` notes) |
| [`codes/`](./codes/) | Solidity interfaces and educational examples |

## Disclaimer

All information (tools, links, articles, text, images, and code) is provided **for educational purposes only**. It is compiled from public sources. You are solely responsible for how you use this material and for any decisions you make; the authors and contributors are not liable for your actions.
