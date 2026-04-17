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

**SEO:** Per-page `description` in front matter, Open Graph / Twitter meta (`overrides/main.html`), `sitemap.xml` (post-build hook), and `docs/robots.txt`. See [Contributing — SEO](./docs/contributing.md#seo-search-and-sharing).

### Publish to GitHub Pages

```bash
mkdocs gh-deploy
```

If you use the included GitHub Actions workflow, pushing to the default branch builds and deploys the site to the `gh-pages` branch.

### Host on Render (subdomain of tekvo.io)

**Production subdomain:** **`blockchain-sec.tekvo.io`** — clearly scoped to blockchain security content while staying short.

Other reasonable options if you change your mind later:

- **`docs.tekvo.io`** — generic documentation hostname.
- **`security.tekvo.io`** — broad security brand line.

This repo includes a **[Render Blueprint](https://render.com/docs/infrastructure-as-code)** at [`render.yaml`](./render.yaml): static runtime, `mkdocs build` → publish directory **`site`**, custom domain **`blockchain-sec.tekvo.io`** (added in Render after first deploy), and basic security headers.

**Steps**

1. In [Render Dashboard](https://dashboard.render.com) → **New** → **Blueprint** (or **Static Site** if you prefer clicking instead of YAML). Connect the **`tekvo/Blockchain-Crypto-Auditing-Security`** repo and select branch **`main`**.
2. If you use the blueprint, Render reads `render.yaml`. Otherwise create a **Static Site** with:
   - **Build command:** `pip install --no-cache-dir -r requirements.txt && mkdocs build --strict`
   - **Publish directory:** `site`
3. After the first deploy, note the default URL (e.g. `https://tekvo-blockchain-security-docs.onrender.com`).
4. In Render → your static service → **Settings** → **Custom domains** → add **`blockchain-sec.tekvo.io`** and follow Render’s DNS instructions (typically a **CNAME** from **`blockchain-sec`** to the `*.onrender.com` hostname they show).
5. In your **DNS host** for `tekvo.io`, create that **CNAME** and wait for TLS provisioning.

`mkdocs.yml` sets **`site_url`** to `https://blockchain-sec.tekvo.io/` for canonical URLs and search; if you use another hostname, update `site_url` (and Render custom domain + DNS) to match.

## Repository layout

| Path | Purpose |
|------|---------|
| [`docs/`](./docs/) | Site source: landing page, guides, [code library](./docs/code/index.md), guided code page |
| [`docs/contributing.md`](./docs/contributing.md) | Maintainer notes: tone, industry generator, snippets, builds |
| [`docs/guides/`](./docs/guides/) | One markdown file per topic (former `001`–`012` notes) |
| [`docs/industry/`](./docs/industry/) | Industry verticals + **catalog IDs** for future use case mapping; regenerate from [`scripts/generate_industry_pages.py`](./scripts/generate_industry_pages.py) where applicable |
| [`codes/`](./codes/) | Solidity interfaces and educational examples |
| [`render.yaml`](./render.yaml) | Render static-site blueprint (optional; use dashboard instead if you prefer) |
| [`mkdocs_hooks.py`](./mkdocs_hooks.py) | Post-build `sitemap.xml` generation |
| [`overrides/main.html`](./overrides/main.html) | Open Graph, Twitter Card, and WebSite JSON-LD |

## Disclaimer

All information (tools, links, articles, text, images, and code) is provided **for educational purposes only**. It is compiled from public sources. You are solely responsible for how you use this material and for any decisions you make; the authors and contributors are not liable for your actions.
