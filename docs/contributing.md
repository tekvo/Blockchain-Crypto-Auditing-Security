# Contributing to this documentation

This page is for **people who edit or extend the site** (Tekvo maintainers, collaborators, or open contributors). Published guides and industry pages are written as **direct Tekvo-provided material** for readers; maintenance and “how to continue” notes live here only.

## Voice and scope

- **Reader-facing pages** state what Tekvo provides, how risks behave, and what practices apply—without asking the reader to edit the doc or replace placeholders.
- **Industry verticals** (`docs/industry/`): substantive copy, composites where anonymized examples help, and stable **catalog IDs** for cross-linking. Detailed instructions for updating stories, testimonials, bios, use-case tables, or contact flows belong in this file—not in callouts on those pages.

## Industry pages

### Hand-maintained vs generated

- **`docs/industry/web3-blockchain-security.md`** is edited by hand.
- The other vertical markdown files under `docs/industry/` are produced by **`scripts/generate_industry_pages.py`** (data in the `INDUSTRIES` list). After changing structure or shared blocks in the script, run:

```bash
python3 scripts/generate_industry_pages.py
```

### Use case catalog

Each industry page exposes a **catalog ID** (see `docs/industry/index.md`). When adding a use case article:

1. Add a row to the **Use case mapping** table on the matching industry page (or extend the generator’s `use_case_block` if rows become data-driven).
2. Reference the same **`catalog_id`** from the use case article so navigation stays consistent.

### Contact and forms

Industry pages use CTAs to **[Tekvo.io](https://www.tekvo.io)** and optional `mailto:` links. To embed a hosted form (HubSpot, Webflow, Formspree, etc.), update the HTML in the generator’s `form_block()` or in `web3-blockchain-security.md`, and test with `mkdocs serve`.

## Guides and security notes (`docs/guides/`)

- Prefer **direct explanations** (what the risk is, what breaks, what mitigations exist) over meta-instructions (“how to use this page”) in the published text.
- Cross-links to related guides are encouraged; keep them factual (“See … for …”).

## Code library (`docs/code/`, `docs/code-samples.md`)

- Snippets are pulled from the repo’s **`codes/`** tree via **pymdownx.snippets** (`--8<--` includes). Changing Solidity under `codes/` requires a **`mkdocs build`** (or `mkdocs serve`) to refresh the built site.
- The Material theme adds **copy-to-clipboard** on code blocks; no separate “tip” is required on reader pages for that behavior.

## Local build

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
mkdocs serve
```

Deployment options:

- **GitHub Pages** — push to `main` / `master` triggers `.github/workflows/docs.yml` (`mkdocs gh-deploy`).
- **Render** — see the root **`render.yaml`** blueprint and the **Host on Render** section in **`README.md`** (production host: `https://blockchain-sec.tekvo.io/`; keep `site_url` in `mkdocs.yml` aligned with the hostname you serve).

## Legal disclaimer (site-wide)

The disclaimer on the [home page](index.md) applies to educational compilation of public material; adjust only with legal review.
