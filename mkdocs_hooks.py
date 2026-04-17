"""MkDocs hooks: post-build sitemap.xml from built HTML (no extra dependencies)."""

from __future__ import annotations

from pathlib import Path
from xml.sax.saxutils import escape


def on_post_build(config, **kwargs) -> None:
    site_url = config.get("site_url")
    if not site_url:
        return

    base = site_url.rstrip("/") + "/"
    site_dir = Path(config["site_dir"])

    locs: list[str] = []
    for path in sorted(site_dir.rglob("index.html")):
        rel = path.parent.relative_to(site_dir)
        if str(rel) == ".":
            loc = base
        else:
            loc = base + rel.as_posix().rstrip("/") + "/"
        locs.append(loc)

    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    ]
    for loc in locs:
        priority = "1.0" if loc.rstrip("/") == base.rstrip("/") else "0.8"
        lines.append("  <url>")
        lines.append(f"    <loc>{escape(loc)}</loc>")
        lines.append("    <changefreq>weekly</changefreq>")
        lines.append(f"    <priority>{priority}</priority>")
        lines.append("  </url>")
    lines.append("</urlset>")

    out = site_dir / "sitemap.xml"
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
