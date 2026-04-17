#!/usr/bin/env python3
"""Generate docs/industry/*.md vertical pages. Run from repo root: python3 scripts/generate_industry_pages.py"""
from __future__ import annotations

from pathlib import Path


def experts_block(roles: list[tuple[str, str, str]]) -> str:
    parts = ['<div class="tekvo-expert-grid" markdown="1">\n']
    for initials, title, subtitle in roles:
        parts.append(
            f"""<div class="tekvo-expert" markdown="1">

<div class="tekvo-expert__avatar" markdown="1">{initials}</div>

<div class="tekvo-expert__body" markdown="1">

### {title}

{subtitle}

</div>

</div>

"""
        )
    parts.append("</div>\n")
    return "".join(parts)


def form_block(slug: str) -> str:
    return f"""
## Request consultation or demo {{: #request-consultation }}

Use the checklist below when you reach out so we can respond with the right lead and a realistic timeline.

**Include in your message**

- **Industry & use case** (product line, geography, pilot vs production)  
- **Blockchain role** (shared ledger, tokenized asset, wallet/custody touchpoint, vendor chain, etc.)  
- **Technical scope** (smart contracts, integrations, key management) and any **fixed vendors or chains**  
- Target **milestone** (design review, procurement gate, launch, audit)  
- Links or docs shareable under **NDA**

<div class="tekvo-form-panel" markdown="1">

<label for="tekvo-intent-{slug}">What are you looking for?</label>
<select id="tekvo-intent-{slug}" name="intent">
  <option>Discovery / scope workshop</option>
  <option>Security or architecture review</option>
  <option>Launch or procurement readiness</option>
  <option>Training and SDLC</option>
  <option>Other</option>
</select>

<label for="tekvo-notes-{slug}">Notes (paste into your email or contact form)</label>
<textarea id="tekvo-notes-{slug}" name="notes" placeholder="Scope, timelines, compliance context, links, NDA."></textarea>

<div class="tekvo-form-panel__actions" markdown="1">

[Continue on Tekvo.io](https://www.tekvo.io){{ .md-button .md-button--primary }}
[Email opening (mailto)](mailto:?subject=Consultation%20%28{slug}%29&body=Industry%20use%20case%20and%20timeline%3A%0A%0A){{ .md-button }}

</div>

<p class="tekvo-muted" markdown="1">**Tekvo.io** hosts the live intake flow; the fields above help organize scope before you continue in the browser or mail client.</p>

</div>

---
[Back to Industry overview](index.md) · [Home](../index.md)
"""


def use_case_block(catalog_id: str, touchpoint_hint: str) -> str:
    return f"""
## Use case mapping

**Catalog ID:** `{catalog_id}` — stable key for this vertical in the site catalog and in cross-references from use case articles.

| Use case | Touchpoint / asset | Notes |
| --- | --- | --- |
| *Listed as articles are published.* | {touchpoint_hint} | — |
"""


def page(meta: dict) -> str:
    slug = meta["slug"]
    title = meta["title"]
    desc = meta["description"]
    hero_title = meta["hero_title"]
    hero_lead = meta["hero_lead"]
    rows = meta["rows"]
    cards = meta["cards"]
    ai_extra = meta["ai_extra"]
    deep = meta["deep_bullets"]
    composite = meta["composite"]
    resources_extra = meta.get("resources_extra", [])
    catalog_id = meta["catalog_id"]
    touch = meta["touchpoint_hint"]
    roles = meta["expert_roles"]

    rows_md = "\n".join(f"| **{a}** | {b} | {c} |" for a, b, c in rows)
    cards_html = '<div class="tekvo-card-grid tekvo-card-grid--3" markdown="1">\n'
    for h3, body in cards:
        cards_html += f"""<div class="tekvo-card" markdown="1">

### {h3}

{body}

</div>

"""
    cards_html += "</div>\n"

    res_extra = "\n".join(f"- {line}" for line in resources_extra)
    res_block = f"\n{res_extra}\n" if res_extra else ""

    deep_md = "\n".join(f"- {b}" for b in deep)

    return f"""---
title: {title}
description: {desc}
---

<div class="tekvo-hero" markdown="1">

# {hero_title}

{hero_lead}

[Request a demo](https://www.tekvo.io){{ .md-button .md-button--primary }}
[Request consultation](#request-consultation){{ .md-button }}

<p class="tekvo-muted" markdown="1">Blockchain may be a **pilot** or **core infrastructure** here; either way, trust boundaries and operational security matter before scale. Deeper technical reference is in the [guides](../guides/blockchain-best-practices.md). **Tekvo.io** scopes commercial engagements separately from this public library.</p>

</div>

## Industry overview and key challenges

| Challenge | Business impact | How Tekvo fits |
| --- | --- | --- |
{rows_md}

## Platform and solutions

{cards_html}

**Capabilities you can combine:** architecture and threat modeling, **integration and key-management** review, vendor / chain selection support, **pre-launch** and **delta** reviews, and executive-ready summaries of residual risk (with counsel where regulated).

## AI and technology adoption in the industry

Teams are adopting **AI for documentation, code assist, and operations**—which accelerates delivery but can skip explicit invariants and cross-party trust analysis. {ai_extra}

**Tekvo’s stance:** pair AI acceleration with **written assumptions, tests, and human review** at integration boundaries—especially where blockchain touches custody, identity, or settlement.

## Solution deep dive and demo

{deep_md}

[Schedule a workshop](https://www.tekvo.io){{ .md-button .md-button--primary }}

## Customer success stories

Illustrative **composite** scenarios—anonymized patterns Tekvo routinely works through with organizations in this sector (not attributed to a single named engagement):

{composite}

## What clients emphasize

Across programs in this vertical, stakeholders most often cite **clear severity ordering**, **actionable remediation** for engineering, and **briefings that translate technical findings** for sponsors, procurement, and partners—without diluting exploitability or residual risk.

## Explore resources

**On this site**

- [Types of blockchain attacks](../guides/blockchain-attacks.md) — network, wallet, bridges, ordering.  
- [Blockchain best practices](../guides/blockchain-best-practices.md) — OWASP-aligned design patterns.  
- [Audit roadmap](../guides/audit-roadmap.md) — internal checklist before external audit.
{res_block}
## Meet our industry experts

Tekvo assigns **delivery leads** matched to sector and technical surface. Typical roles include:

{experts_block(roles)}
{use_case_block(catalog_id, touch)}
{form_block(slug)}
"""


INDUSTRIES: list[dict] = [
    {
        "slug": "banking-payments-fintech",
        "file": "banking-payments-fintech.md",
        "catalog_id": "banking-payments-fintech",
        "title": "Banking, payments & FinTech",
        "description": "Blockchain security and readiness for banks, payment networks, and FinTech using or evaluating DLT.",
        "hero_title": "Move from blockchain pilot to production with clear risk ownership",
        "hero_lead": "**Stablecoins, settlement experiments, custodial wallets, and partner-led networks** each change where funds can leak or where regulators ask for evidence. Tekvo helps you **document trust boundaries**, **review integrations and contracts**, and **align security work** with procurement and audit cycles.",
        "rows": [
            (
                "Regulatory and audit evidence",
                "Supervisors and partners expect repeatable controls—not only a vendor slide deck.",
                "Map controls to **architecture and operational reality**; produce review artifacts suitable for second-line and external audit.",
            ),
            (
                "Custody and key lifecycle",
                "A single weak ceremony undermines the whole ledger story.",
                "Review **key management**, signing paths, and disaster recovery for on-chain and vendor-held assets.",
            ),
            (
                "Vendor and chain lock-in",
                "Wrong base layer or integration partner becomes expensive to unwind.",
                "**Architecture and exit** review before long-term commitments.",
            ),
            (
                "Legacy + DLT interoperability",
                "Message bridges and APIs multiply attack surface.",
                "**Integration threat modeling** with emphasis on settlement finality and replay.",
            ),
        ],
        "cards": [
            (
                "DLT settlement & messaging",
                "Assurance for **corridors**, **atomic settlement** designs, and interfaces to core banking or PSP systems.",
            ),
            (
                "Wallet & custody touchpoints",
                "Review of **hot/cold** flows, policy engines, and **smart contract** hooks where customer funds move.",
            ),
            (
                "Program readiness",
                "**Procurement- and audit-friendly** documentation, test evidence, and remediation tracking.",
            ),
        ],
        "ai_extra": "FinTech teams often generate integration code quickly; blockchain adds **irreversibility**, so review gates must catch errors before they hit shared environments.",
        "deep_bullets": [
            "**Settlement invariants** — what must be true before funds move between parties, chains, and nostro/vostro representations?",
            "**Third-party reliance** — oracle, bridge, KYC, or chain RPC failures and how your product degrades safely.",
            "**Evidence pack** — what engineering can show risk and compliance stakeholders after each release.",
        ],
        "composite": "**Composite — cross-border payment pilot**\n\n- **Situation:** Consortium DLT with multiple bank nodes; new smart contract module for liquidity netting.  \n- **Outcome:** Access-control and upgrade review before go-live; **residual risk memo** for sponsor bank board pack.",
        "resources_extra": [
            "**External (education)** — [BIS innovation hub](https://www.bis.org/about/bisih/topics/dlt.htm) for central-bank DLT context (informational, not advice).",
        ],
        "touchpoint_hint": "Core banking interfaces, custodial wallets, stablecoin or settlement contracts, partner nodes",
        "expert_roles": [
            ("FS", "Financial services lead", "**Regulatory-aware** architecture and security narrative."),
            ("PM", "Program lead", "Coordinates **diligence**, vendors, and milestone reviews."),
        ],
    },
    {
        "slug": "capital-markets-tokenization",
        "file": "capital-markets-tokenization.md",
        "catalog_id": "capital-markets-tokenization",
        "title": "Capital markets & tokenization",
        "description": "Security for tokenized securities, fund instruments, and market infrastructure touching blockchain.",
        "hero_title": "Tokenize assets without hiding risk in the plumbing",
        "hero_lead": "**Primary issuance, secondary trading, and corporate actions** on-chain require the same rigor as traditional market infrastructure—plus new surfaces around **contracts, oracles, and custody**. Tekvo helps issuers and venues **clarify what is enforced on-chain vs off-chain** and **harden the technical path to liquidity**.",
        "rows": [
            (
                "Legal–technical alignment",
                "Misaligned representations between prospectus and code create liability.",
                "Review **behavior vs disclosure** for critical user journeys and admin actions.",
            ),
            (
                "Liquidity and DeFi touchpoints",
                "AMM or lending integrations introduce MEV and oracle risk.",
                "**Economic and ordering** threat modeling for connected pools.",
            ),
            (
                "Corporate actions & lifecycle",
                "Splits, dividends, and defaults are error-prone when split across systems.",
                "Trace **state transitions** and privileged operations across modules.",
            ),
            (
                "Surveillance and reporting",
                "On-chain opacity can break surveillance expectations.",
                "Document **visibility** and monitoring hooks for compliance tech.",
            ),
        ],
        "cards": [
            (
                "Issuance & cap table logic",
                "Review of **mint/burn**, **transfers with restrictions**, and **admin** roles.",
            ),
            (
                "Trading & settlement links",
                "Assessment of **DEX/CeFi** integrations, bridges, and **settlement finality** assumptions.",
            ),
            (
                "Infrastructure upgrades",
                "**Proxy and upgrade** paths for contracts serving live instruments.",
            ),
        ],
        "ai_extra": "AI is used for **document extraction** and **pricing analytics**; on-chain, models do not replace **invariant checks** on supply, permissions, and settlement flags.",
        "deep_bullets": [
            "**Instrument invariants** — supply, eligibility, and transfer rules that must hold under adversarial trading.",
            "**Oracle and reference data** — how prices and corporate actions enter the system.",
            "**Operational controls** — who can pause, upgrade, or migrate user positions—and under what delay.",
        ],
        "composite": "**Composite — fund tokenization module**\n\n- **Situation:** Upgrade to subscription/redemption contract before new share class.  \n- **Outcome:** Storage layout and **access control** delta review; test plan gaps closed before external audit.",
        "resources_extra": [
            "**External** — [IOSCO](https://www.iosco.org/) publications for securities regulation context (informational).",
        ],
        "touchpoint_hint": "Token contracts, transfer restrictions, trading venues, custody adapters, oracles",
        "expert_roles": [
            ("CM", "Markets infrastructure lead", "**Trading and settlement** aware reviews."),
            ("TK", "Tokenization architect", "Links **instrument design** to contract behavior."),
        ],
    },
    {
        "slug": "insurance",
        "file": "insurance.md",
        "catalog_id": "insurance",
        "title": "Insurance",
        "description": "Blockchain for parametric products, claims, reinsurance, and fraud-resistant records—with security at the core.",
        "hero_title": "Automate claims and coverage without automating new loss vectors",
        "hero_lead": "**Parametric triggers, proof-of-loss attestations, and consortium ledgers** can reduce friction—but they concentrate trust in **oracles, multisigs, and contract upgrades**. Tekvo helps carriers and MGAs **validate trigger logic**, **third-party data feeds**, and **governance** before policies scale.",
        "rows": [
            (
                "Oracle and attestation risk",
                "Bad or stale data pays claims incorrectly.",
                "Model **oracle failure** and manipulation; define safe degradation.",
            ),
            (
                "Fraud and gaming",
                "Public mempools and composability enable coordinated abuse.",
                "**Economic attack** review for payout paths.",
            ),
            (
                "Consortium governance",
                "Weak member controls let one party alter parameters.",
                "**Governance and upgrade** review across participants.",
            ),
            (
                "Legacy core integration",
                "API and batch bridges can desync policy state.",
                "**Reconciliation and replay** analysis.",
            ),
        ],
        "cards": [
            (
                "Parametric & claims contracts",
                "Review of **trigger math**, **payout caps**, and **emergency** controls.",
            ),
            (
                "Reinsurance & bordereaux",
                "Security for **batch settlements** and **privacy** where data crosses firms.",
            ),
            (
                "Fraud analytics handoff",
                "Alignment between **on-chain events** and investigation workflows.",
            ),
        ],
        "ai_extra": "Insurers use AI for **fraud scoring** and **underwriting**; when triggers blend ML outputs with chain logic, **provenance and override** paths need explicit review.",
        "deep_bullets": [
            "**Payout invariants** — caps, deductibles, double-pay prevention across channels.",
            "**Data lineage** — how external events become on-chain facts.",
            "**BCP** — behavior during oracle outages, chain congestion, or bridge pauses.",
        ],
        "composite": "**Composite — weather parametric pilot**\n\n- **Situation:** New oracle feed and payout contract for a narrow geography.  \n- **Outcome:** **Staleness and manipulation** scenarios documented; insurer retained clear **go / no-go** criteria.",
        "resources_extra": [],
        "touchpoint_hint": "Claims contracts, oracle adapters, attestation verifiers, consortium nodes",
        "expert_roles": [
            ("IN", "Insurance domain lead", "**Product and claims** aware security."),
            ("OR", "Oracle & data lead", "Feeds, attestations, and **fallback** design."),
        ],
    },
    {
        "slug": "supply-chain-logistics",
        "file": "supply-chain-logistics.md",
        "catalog_id": "supply-chain-logistics",
        "title": "Supply chain, logistics & trade",
        "description": "Provenance, trade finance, and multi-party ledgers across suppliers, ports, and financiers.",
        "hero_title": "Prove origin and handoffs—without brittle trust assumptions",
        "hero_lead": "**Bill of lading, EPCIS events, and inventory tokens** often sit between ERPs, IoT gateways, and **multi-party chains**. Tekvo helps you **separate cryptographic proof from business attestation**, **review smart contracts and APIs**, and **prepare for disputes** when events conflict.",
        "rows": [
            (
                "Physical–digital gap",
                "Sensors and humans can lie; blockchain does not fix bad inputs.",
                "Threat model **who attests what** and **revocation** behavior.",
            ),
            (
                "Multi-party visibility",
                "Competitors share a network; data leaks are existential.",
                "**Privacy, channels, and access** review.",
            ),
            (
                "Trade finance integration",
                "Banks expect clear settlement and document control.",
                "**Interoperability** and **finality** across systems.",
            ),
            (
                "Long-lived assets",
                "Contracts outlive vendors; upgrades must be governable.",
                "**Upgrade and custody** paths for long-running networks.",
            ),
        ],
        "cards": [
            (
                "Provenance & traceability",
                "Event models, **hashes vs on-chain payloads**, and verifier logic.",
            ),
            (
                "Trade & inventory tokens",
                "Tokenized documents and **collateral** representations.",
            ),
            (
                "Partner onboarding",
                "**Identity, roles, and certificates** for nodes and APIs.",
            ),
        ],
        "ai_extra": "Computer vision and NLP assist **document capture**; pairing that with on-chain anchors requires **clear liability** when extraction errors propagate.",
        "deep_bullets": [
            "**Attestation model** — issuers, verifiers, and revocation.",
            "**Dispute flows** — how conflicting events are resolved on- and off-chain.",
            "**Integration surface** — ERP, TMS, and IoT gateways.",
        ],
        "composite": "**Composite — cold-chain consortium**\n\n- **Situation:** New member integration exposed a shared contract admin pattern.  \n- **Outcome:** **Role separation** and timelock recommendations before production volume.",
        "resources_extra": [],
        "touchpoint_hint": "Event registries, document hashes, inventory tokens, bank APIs",
        "expert_roles": [
            ("SC", "Supply chain lead", "**Multi-party** process and data design."),
            ("LG", "Logistics integration", "APIs, **IoT**, and edge security."),
        ],
    },
    {
        "slug": "healthcare-life-sciences",
        "file": "healthcare-life-sciences.md",
        "catalog_id": "healthcare-life-sciences",
        "title": "Healthcare & life sciences",
        "description": "Clinical trial integrity, credentialing, supply chain of medicines, and patient-data minimization with DLT.",
        "hero_title": "Use ledgers where they strengthen trust—not where they leak PHI",
        "hero_lead": "**Trial consent, device registries, and pharma anti-counterfeiting** can benefit from tamper-evident records—but **privacy, HIPAA/GDPR, and clinical validity** dominate. Tekvo helps teams **minimize on-chain data**, **review access paths**, and **secure integrations** with EHRs and CRO systems.",
        "rows": [
            (
                "Privacy and re-identification",
                "Hashes and metadata can still identify patients.",
                "**Data minimization** and cryptography review.",
            ),
            (
                "Clinical and regulatory evidence",
                "Regulators ask how integrity is demonstrated.",
                "Map technical controls to **GCP / quality** narratives.",
            ),
            (
                "Device and trial IoT",
                "Compromised devices poison the ledger.",
                "**Endpoint and attestation** modeling.",
            ),
            (
                "Partner data sharing",
                "Cross-hospital networks multiply breach impact.",
                "**Channel security** and key governance.",
            ),
        ],
        "cards": [
            (
                "Consent & trial integrity",
                "Anchors, **hashes**, and **immutable logs** without unnecessary PHI exposure.",
            ),
            (
                "Pharma serialization",
                "Handoff between **manufacturer, wholesaler, dispenser** systems and chain.",
            ),
            (
                "Credentialing & workforce",
                "Verifiable credentials and **revocation** patterns.",
            ),
        ],
        "ai_extra": "Clinical NLP and imaging AI produce **derived artifacts**; anchoring them on-chain needs **policy on what is hashed** and who can correlate.",
        "deep_bullets": [
            "**PHI boundary** — what never touches the chain vs what is aggregated.",
            "**Provenance chain** — from sensor or clinician to anchor.",
            "**Break-glass** — emergency access without silent corruption.",
        ],
        "composite": "**Composite — trial consent anchoring**\n\n- **Situation:** Vendor proposed storing expanded metadata on a public testnet.  \n- **Outcome:** **Architecture pivot** to minimal hashes + off-chain vault; security sign-off for IRB pack.",
        "resources_extra": [
            "**External** — [FDA digital health](https://www.fda.gov/medical-devices/digital-health-center-excellence) for context (not legal advice).",
        ],
        "touchpoint_hint": "Consent anchors, serialization events, credential issuers, research data APIs",
        "expert_roles": [
            ("HC", "Healthcare lead", "**Privacy-first** architecture."),
            ("LS", "Life sciences PM", "CRO / sponsor **milestone** alignment."),
        ],
    },
    {
        "slug": "energy-sustainability-commodities",
        "file": "energy-sustainability-commodities.md",
        "catalog_id": "energy-sustainability-commodities",
        "title": "Energy, sustainability & commodities",
        "description": "RECs, carbon credits, grid-edge flexibility, and commodity traceability on shared ledgers.",
        "hero_title": "Make environmental markets auditable—not gameable",
        "hero_lead": "**Tokenized credits, prosumer settlements, and grid flexibility markets** attract **double-counting, oracle gaming, and bridge risk** when bridged to liquid DeFi. Tekvo helps design and review **mint/burn rules**, **MRV integrations**, and **governance** so environmental claims hold up to scrutiny.",
        "rows": [
            (
                "MRV integrity",
                "Weak measurement undermines the entire market.",
                "Review **oracle and batch** ingestion; adversarial scenarios.",
            ),
            (
                "Double issuance / retirement",
                "Splits across registries and chains create arbitrage.",
                "**Supply invariant** analysis across systems.",
            ),
            (
                "DeFi composability",
                "Secondary markets amplify manipulation.",
                "**Economic** review of pools and oracles.",
            ),
            (
                "Physical settlement",
                "Delivery and scheduling interfaces are attackable.",
                "**Ops and API** threat modeling.",
            ),
        ],
        "cards": [
            (
                "Credit lifecycle contracts",
                "**Issuance, transfer, retirement**, and **audit trails**.",
            ),
            (
                "Grid / flexibility programs",
                "**Settlement** timing and **device** identity.",
            ),
            (
                "Commodity provenance",
                "Batches, **BL** events, and **financing** hooks.",
            ),
        ],
        "ai_extra": "Remote sensing and ML drive **MRV**; on-chain claims must encode **confidence and revision** without silent retroactive edits that break market rules.",
        "deep_bullets": [
            "**Issuance invariants** — no double-mint across bridges and legacy registries.",
            "**Oracle policy** — staleness, disputes, and manual override with evidence.",
            "**Governance** — who can change methodology parameters.",
        ],
        "composite": "**Composite — voluntary carbon bridge**\n\n- **Situation:** Bridge to high-liquidity chain before COP marketing push.  \n- **Outcome:** **Replay and supply cap** review; emergency pause criteria tied to oracle divergence.",
        "resources_extra": [],
        "touchpoint_hint": "Credit tokens, retirement registries, MRV pipelines, market routers",
        "expert_roles": [
            ("EN", "Energy markets lead", "**Physical and financial** settlement context."),
            ("ES", "Sustainability data", "**MRV** and environmental claim integrity."),
        ],
    },
    {
        "slug": "government-public-sector",
        "file": "government-public-sector.md",
        "catalog_id": "government-public-sector",
        "title": "Government & public sector",
        "description": "Digital identity, land registries, benefits, and inter-agency records with blockchain or DLT pilots.",
        "hero_title": "Serve citizens with transparent systems—and controlled change",
        "hero_lead": "**Verifiable credentials, land titles, and benefits distribution** demand **accessibility, auditability, and long-term vendor independence**. Tekvo helps agencies and integrators **review chain and contract choices**, **key ceremonies**, and **upgrade governance** aligned to procurement rules.",
        "rows": [
            (
                "Vendor and chain longevity",
                "Citizen records outlive vendors.",
                "**Exit, export, and migration** planning.",
            ),
            (
                "Equity and accessibility",
                "Complex wallets exclude users.",
                "**UX and custody** risk as a security topic.",
            ),
            (
                "Inter-agency trust",
                "Federated models hide single points of compromise.",
                "**Federation and admin** review.",
            ),
            (
                "Transparency vs privacy",
                "Open ledgers can expose sensitive patterns.",
                "**Data placement** and minimization.",
            ),
        ],
        "cards": [
            (
                "Identity & credentials",
                "**Issuance, revocation**, and **wallet** security.",
            ),
            (
                "Registries & titles",
                "**Immutability vs correction** workflows and authority.",
            ),
            (
                "Benefits & disbursement",
                "**Fraud resistance** and **audit** trails.",
            ),
        ],
        "ai_extra": "Agencies pilot **AI copilots** for casework; any auto-anchoring to a ledger needs **human override**, logging, and bias review—not only IT security.",
        "deep_bullets": [
            "**Authority model** — who can correct errors and how that is logged.",
            "**Key ceremony** — generation, backup, and rotation for national-scale systems.",
            "**Procurement artifacts** — security evidence suitable for oversight bodies.",
        ],
        "composite": "**Composite — digital ID wallet pilot**\n\n- **Situation:** Wallet vendor change mid-pilot risked different key storage.  \n- **Outcome:** **Migration and recovery** review; citizen-facing incident playbook drafted.",
        "resources_extra": [],
        "touchpoint_hint": "Credential issuers, registry contracts, disbursement modules, agency APIs",
        "expert_roles": [
            ("GV", "Public sector lead", "**Procurement and oversight** language."),
            ("ID", "Digital identity architect", "**Wallet and federation** security."),
        ],
    },
    {
        "slug": "telecom-identity",
        "file": "telecom-identity.md",
        "catalog_id": "telecom-identity",
        "title": "Telecom, identity & consumer data",
        "description": "eSIM, number portability, decentralized identity, and carrier-grade Web3 experiments.",
        "hero_title": "Anchor identity where subscribers expect reliability",
        "hero_lead": "**Wallet-based logins, roaming settlements, and DID** projects sit next to **SS7/Diameter-era threats** and modern **API fraud**. Tekvo helps telcos and identity providers **review custody models**, **smart contract–backed credentials**, and **fraud monitoring** across legacy and DLT stacks.",
        "rows": [
            (
                "Subscriber safety",
                "SIM-swap and phishing move to seed phrases.",
                "**Recovery and custody** UX as security.",
            ),
            (
                "Roaming and settlement",
                "DLT pilots must not break reconciliation SLAs.",
                "**Performance and finality** analysis.",
            ),
            (
                "Partner ecosystems",
                "MVNOs and hyperscalers expand blast radius.",
                "**B2B2C trust** boundaries.",
            ),
            (
                "Regulatory capture",
                "KYC/AML data on-chain is rarely appropriate.",
                "**Data minimization** and **off-chain** patterns.",
            ),
        ],
        "cards": [
            (
                "Wallet & DID programs",
                "**Key management**, recovery, and **credential** revocation.",
            ),
            (
                "Settlement pilots",
                "**Throughput**, **privacy**, and **settlement** guarantees.",
            ),
            (
                "Fraud operations",
                "Signals from **on-chain** and **legacy** fraud stacks.",
            ),
        ],
        "ai_extra": "LLM-powered support can leak **PII** into prompts; pairing with on-chain identifiers raises **tracing** risk—policy and technical guardrails together.",
        "deep_bullets": [
            "**Recovery threat model** — social recovery, help desks, and law enforcement requests.",
            "**Interconnect** — APIs between billing, OSS/BSS, and chain nodes.",
            "**Abuse handling** — freezes, reversals (where legally possible), and transparency.",
        ],
        "composite": "**Composite — DID wallet partnership**\n\n- **Situation:** Third-party wallet held subscriber keys for a loyalty token.  \n- **Outcome:** **Contract + custody** review; contractual security SLAs drafted.",
        "resources_extra": [
            "**External** — [W3C DID](https://www.w3.org/TR/did-core/) for standards context.",
        ],
        "touchpoint_hint": "DID methods, wallet SDKs, roaming settlement contracts, fraud APIs",
        "expert_roles": [
            ("TL", "Telecom lead", "**Carrier-scale** operations and reliability."),
            ("DI", "Identity architect", "**Credentials** and subscriber safety."),
        ],
    },
    {
        "slug": "retail-consumer-brands",
        "file": "retail-consumer-brands.md",
        "catalog_id": "retail-consumer-brands",
        "title": "Retail, loyalty & consumer brands",
        "description": "Loyalty tokens, NFT drops, supply transparency, and omnichannel Web3 experiments.",
        "hero_title": "Turn loyalty and collectibles into trust—not support tickets",
        "hero_lead": "**NFT drops, tokenized loyalty, and “phygital” claims** create **wallet, contract, and marketplace** risk in front of mass consumers. Tekvo helps brands **review mint and royalty logic**, **partner marketplaces**, and **incident comms** before campaigns scale.",
        "rows": [
            (
                "Brand and PR risk",
                "One exploit becomes headline news.",
                "**Pre-launch** review and **playbooks**.",
            ),
            (
                "Partner marketplaces",
                "Users blame the brand when a DEX misbehaves.",
                "**Integration and slippage** guidance.",
            ),
            (
                "Counterfeits and gray markets",
                "On-chain provenance must match physical reality.",
                "**Attestation** model review.",
            ),
            (
                "Global compliance",
                "Securities and gambling rules vary by market.",
                "**Geofencing and disclosures** with counsel.",
            ),
        ],
        "cards": [
            (
                "Campaign contracts",
                "**Mint caps**, **allowlists**, **royalties**, and **admin** roles.",
            ),
            (
                "Wallet & custodial partners",
                "**SDK** and **key** handling for mainstream users.",
            ),
            (
                "Marketplace integrations",
                "**Listing**, **pricing**, and **MEV** awareness for drops.",
            ),
        ],
        "ai_extra": "Generative tools speed **creative and contract** iteration; without checklist discipline, **misconfigured royalties** and **metadata** bugs ship fast.",
        "deep_bullets": [
            "**Customer journey** — where funds and keys move end-to-end.",
            "**Partner SLAs** — who patches a vulnerability in shared contracts.",
            "**Rollback** — what happens if metadata or royalty parameters were wrong at T0.",
        ],
        "composite": "**Composite — global loyalty token**\n\n- **Situation:** Multi-region launch with different tax treatment.  \n- **Outcome:** **Transfer restrictions** and admin role review before marketing spend.",
        "resources_extra": [],
        "touchpoint_hint": "Loyalty contracts, NFT collections, marketplace routers, custodial wallets",
        "expert_roles": [
            ("RB", "Retail & brand lead", "**Campaign-scale** security."),
            ("UX", "Consumer safety", "**Wallet** and support path modeling."),
        ],
    },
    {
        "slug": "gaming-media-entertainment",
        "file": "gaming-media-entertainment.md",
        "catalog_id": "gaming-media-entertainment",
        "title": "Gaming, media & entertainment",
        "description": "In-game assets, marketplaces, esports, and creator economies with on-chain components.",
        "hero_title": "Protect player economies and creator revenue",
        "hero_lead": "**Marketplaces, crafting systems, and UGC royalties** on-chain inherit **MEV, botting, and rug** dynamics from DeFi—often with younger audiences. Tekvo helps studios **review economy contracts**, **anti-cheat interfaces**, and **live ops** upgrade paths.",
        "rows": [
            (
                "Economy exploits",
                "Duplication bugs destroy trust overnight.",
                "**Invariant testing** for item and currency flows.",
            ),
            (
                "Botting and RMT",
                "On-chain markets attract automated abuse.",
                "**Rate limits**, **signatures**, and **game server** trust boundaries.",
            ),
            (
                "Platform fees and royalties",
                "Players perceive hidden drains as fraud.",
                "**Transparent fee** and **admin** review.",
            ),
            (
                "Cross-game interoperability",
                "Composable items increase attack surface.",
                "**Bridge and metadata** review.",
            ),
        ],
        "cards": [
            (
                "Item & currency contracts",
                "**Mint/burn**, **trades**, and **sinks**.",
            ),
            (
                "Marketplace & matchmaking hooks",
                "**Escrow**, **fees**, and **cancellation** paths.",
            ),
            (
                "Live ops & upgrades",
                "**Hotfix** governance without silent player loss.",
            ),
        ],
        "ai_extra": "AI assists **NPC behavior and moderation**; tying rewards to chain txs needs **anti-sybil** thinking when bots can farm.",
        "deep_bullets": [
            "**Economy invariants** — no duped supply through edge-case trades.",
            "**Player key model** — custodial vs self-custody tradeoffs.",
            "**Incident response** — how to pause or patch without locking funds illegally.",
        ],
        "composite": "**Composite — tradable cosmetic drop**\n\n- **Situation:** Crafting contract interacted with legacy inventory DB.  \n- **Outcome:** **Race and reentrancy** review; server-oracle trust boundary documented.",
        "resources_extra": [],
        "touchpoint_hint": "Game contracts, marketplaces, RNG or VRF hooks, bridge to L2",
        "expert_roles": [
            ("GM", "Gaming economy lead", "**Live ops** aware security."),
            ("CR", "Creator economy", "**Royalty** and marketplace integrations."),
        ],
    },
    {
        "slug": "real-estate-construction",
        "file": "real-estate-construction.md",
        "catalog_id": "real-estate-construction",
        "title": "Real estate, construction & prop-tech",
        "description": "Tokenized ownership, rent streams, construction milestones, and lien transparency.",
        "hero_title": "Record titles and cash flows with enforceable rules",
        "hero_lead": "**Fractional ownership, escrow milestones, and construction bonds** on-chain still depend on **off-chain legal enforcement** and **oracle truth**. Tekvo helps **align contracts with legal intent**, **review escrow and payout logic**, and **secure integrations** with banks and notaries.",
        "rows": [
            (
                "Legal enforceability gap",
                "Smart contracts are not self-carrying legal instruments everywhere.",
                "**Behavior vs deed** mapping with counsel.",
            ),
            (
                "Lien and priority errors",
                "Wrong ordering harms lenders and buyers.",
                "**Priority and payout** state machine review.",
            ),
            (
                "Oracle for inspections",
                "Photos and sign-offs can be faked.",
                "**Attestation** and dispute design.",
            ),
            (
                "Long project timelines",
                "Teams and vendors churn; keys must survive.",
                "**Custody and multisig** for project accounts.",
            ),
        ],
        "cards": [
            (
                "Escrow & milestone payouts",
                "**Conditional release**, **dispute**, and **fee** clarity.",
            ),
            (
                "Tokenized interests",
                "**Transfer restrictions** and **cap table** sync.",
            ),
            (
                "Construction supply",
                "Delivery proofs tied to **payments**.",
            ),
        ],
        "ai_extra": "Computer vision for **site progress** can feed oracles; define **human appeal** when models disagree with contractors.",
        "deep_bullets": [
            "**Payout graph** — who gets paid when, under which proofs.",
            "**Upgrade policy** — who can change milestone parameters mid-build.",
            "**Privacy** — tenant and borrower data minimization.",
        ],
        "composite": "**Composite — rental revenue token**\n\n- **Situation:** Oracle relied on single property manager API.  \n- **Outcome:** **Fallback and manual override** path with audit log; investor memo updated.",
        "resources_extra": [],
        "touchpoint_hint": "Escrow contracts, title tokens, inspection oracles, bank disbursements",
        "expert_roles": [
            ("RE", "Real estate lead", "**Capital stack** and investor narrative."),
            ("CN", "Construction PM", "**Milestone** and vendor integrations."),
        ],
    },
    {
        "slug": "manufacturing-iot-industrial",
        "file": "manufacturing-iot-industrial.md",
        "catalog_id": "manufacturing-iot-industrial",
        "title": "Manufacturing, IoT & industrial",
        "description": "Digital twins, maintenance records, and industrial data markets with DLT.",
        "hero_title": "Bind physical operations to digital truth—safely",
        "hero_lead": "**Maintenance NFTs, quality attestations, and cross-factory data sharing** need **device trust**, **segmented networks**, and **long-lived keys**. Tekvo reviews **edge-to-chain** paths, **contract logic**, and **OT/IT** boundaries for industrial programs.",
        "rows": [
            (
                "Device compromise",
                "One gateway can forge plant-wide events.",
                "**Device identity** and secure boot alignment.",
            ),
            (
                "Legacy OT exposure",
                "Blockchain nodes do not belong directly on PLCs.",
                "**Segmentation** and broker patterns.",
            ),
            (
                "IP leakage",
                "Shared ledgers can expose process parameters.",
                "**Privacy** techniques and off-chain data.",
            ),
            (
                "Vendor sprawl",
                "Integrators rotate; documentation decays.",
                "**Runbooks** and **key** ownership clarity.",
            ),
        ],
        "cards": [
            (
                "Attestation pipelines",
                "**Sensor to anchor** integrity and latency.",
            ),
            (
                "Digital twin linkage",
                "**Hashing** vs on-chain storage tradeoffs.",
            ),
            (
                "Supply and warranty tokens",
                "**Claims** and **recall** workflows.",
            ),
        ],
        "ai_extra": "Predictive maintenance models feed **oracles**; adversarial inputs from compromised sensors become **on-chain facts** unless bounded.",
        "deep_bullets": [
            "**Trust ladder** — device, edge broker, enterprise, chain.",
            "**Safety interlocks** — chain actions must not bypass physical safety systems.",
            "**Lifecycle** — certificate rotation and firmware update security.",
        ],
        "composite": "**Composite — quality attestation network**\n\n- **Situation:** New OEM node class with different TLS stack.  \n- **Outcome:** **Mutual TLS and chain admission** review; anomaly monitoring recommendations.",
        "resources_extra": [
            "**External** — [IEC 62443](https://webstore.iec.ch/) OT security framing (informational).",
        ],
        "touchpoint_hint": "IoT gateways, twin registries, warranty contracts, MES/ERP APIs",
        "expert_roles": [
            ("MF", "Manufacturing lead", "**OT/IT** boundary experience."),
            ("IOT", "IoT security", "**Device** identity and firmware."),
        ],
    },
    {
        "slug": "transportation-mobility",
        "file": "transportation-mobility.md",
        "catalog_id": "transportation-mobility",
        "title": "Transportation & mobility",
        "description": "Fleet credentials, mobility payments, MaaS, and autonomous-vehicle data markets.",
        "hero_title": "Keep mobility payments and credentials moving—without silent trust shifts",
        "hero_lead": "**MaaS wallets, fleet charging, and V2X data markets** blend **high-frequency payments** with **identity**. Tekvo helps operators **review payment and credential contracts**, **roaming settlements**, and **fraud controls** where blockchain is in the path.",
        "rows": [
            (
                "Safety-critical vs payments",
                "Mixing control and payment domains is dangerous.",
                "**Domain separation** architecture.",
            ),
            (
                "Roaming and interoperability",
                "Partner APIs are brittle under attack.",
                "**Auth and replay** review.",
            ),
            (
                "User funds in transit",
                "Wallet bugs strand riders.",
                "**Custody and recovery** patterns.",
            ),
            (
                "Data monetization ethics",
                "Location traces are sensitive.",
                "**Minimization** and consent flows.",
            ),
        ],
        "cards": [
            (
                "Mobility wallets & passes",
                "**Issuance, transfer**, and **revocation**.",
            ),
            (
                "Charging / toll settlement",
                "**Micropayment** channels and **oracle** timing.",
            ),
            (
                "Fleet and OEM data",
                "**B2B** contracts for telemetry sales.",
            ),
        ],
        "ai_extra": "Route and demand forecasting AI influences **pricing oracles**; guard against **feedback loops** that hurt fairness or safety margins.",
        "deep_bullets": [
            "**Payment finality** — what happens when chain or RPC is down mid-trip.",
            "**Partner trust** — who can alter tariffs or credential rules.",
            "**Incident playbooks** — loss of keys vs fraudulent charges.",
        ],
        "composite": "**Composite — MaaS wallet pilot**\n\n- **Situation:** City required open APIs to multiple mobility providers.  \n- **Outcome:** **OAuth + on-chain pass** binding review; abuse scenarios documented.",
        "resources_extra": [],
        "touchpoint_hint": "Mobility wallets, settlement contracts, OEM telematics APIs",
        "expert_roles": [
            ("MO", "Mobility lead", "**Operator and city** programs."),
            ("PY", "Payments architect", "**Micropayment** and channel security."),
        ],
    },
    {
        "slug": "agriculture-food",
        "file": "agriculture-food.md",
        "catalog_id": "agriculture-food",
        "title": "Agriculture & food systems",
        "description": "Farm-to-fork traceability, cooperatives, insurance, and carbon claims for growers.",
        "hero_title": "Give farmers and buyers shared truth—not extra burden",
        "hero_lead": "**Cooperative ledgers, export certifications, and regenerative finance** depend on **trusted field data** and **simple UX**. Tekvo helps **design minimal on-chain footprints**, **review incentive contracts**, and **secure partner integrations** for agtech stacks.",
        "rows": [
            (
                "Connectivity and cost",
                "Low bandwidth farms cannot run full nodes.",
                "**Light client** and **proxy** patterns.",
            ),
            (
                "Truth at the field edge",
                "Cheap sensors and manual entry are gamed.",
                "**Attestation hierarchy** design.",
            ),
            (
                "Co-op governance",
                "Democratic parameter changes need clarity.",
                "**Voting and upgrade** review.",
            ),
            (
                "Carbon stacking",
                "Same practice claimed on multiple programs.",
                "**Cross-registry** integrity.",
            ),
        ],
        "cards": [
            (
                "Cooperative records",
                "**Member equity**, **payouts**, and **votes**.",
            ),
            (
                "Export and certification",
                "**Document** anchors and verifier APIs.",
            ),
            (
                "Parametric crop insurance hooks",
                "**Oracle** design with agronomic advisors.",
            ),
        ],
        "ai_extra": "Satellite and drone ML supports **MRV**; align model updates with **on-chain parameter governance** to avoid silent credit inflation.",
        "deep_bullets": [
            "**Data cost model** — who pays gas and storage across seasons.",
            "**Fraud model** — collusion among smallholders vs inspectors.",
            "**Disaster recovery** — lost devices and seasonal staff turnover.",
        ],
        "composite": "**Composite — cooperative payout token**\n\n- **Situation:** SMS-based signing for low-tech members.  \n- **Outcome:** **Threat model** for SIM swap and help-desk takeover; mitigations prioritized.",
        "resources_extra": [],
        "touchpoint_hint": "Co-op contracts, certification APIs, insurance triggers, carbon MRV",
        "expert_roles": [
            ("AG", "Ag systems lead", "**Field reality** aware design."),
            ("FC", "Food supply chain", "**Export** and retailer integrations."),
        ],
    },
    {
        "slug": "professional-services-legal-ip",
        "file": "professional-services-legal-ip.md",
        "catalog_id": "professional-services-legal-ip",
        "title": "Professional services, legal & IP",
        "description": "Law firms, accounting networks, and IP registries using blockchain for proofs and workflow.",
        "hero_title": "Make cryptographic proofs admissible in workflow—not magic",
        "hero_lead": "**Notarization, discovery hashes, and IP timestamping** require **clear chain-of-custody** from document to anchor. Tekvo helps firms **select architectures**, **review client-facing wallet flows**, and **avoid over-claiming** what a ledger proves.",
        "rows": [
            (
                "Evidentiary standards",
                "Courts care about process, not buzzwords.",
                "**Chain of custody** documentation.",
            ),
            (
                "Client confidentiality",
                "Public chains rarely fit raw documents.",
                "**Hashing and encryption** patterns.",
            ),
            (
                "Conflicts and liability",
                "Who is responsible if an anchor is wrong?",
                "**Service agreements** alignment.",
            ),
            (
                "Vendor hype",
                "Blockchain may not be the simplest tool.",
                "**Honest fit** assessment.",
            ),
        ],
        "cards": [
            (
                "Proof-of-existence services",
                "**Timestamping**, **hashing**, and **key** control.",
            ),
            (
                "Smart contract–backed agreements",
                "**Escrow**, **milestones**, and **dispute** hooks.",
            ),
            (
                "Consortium networks between firms",
                "**Governance** and **member exit**.",
            ),
        ],
        "ai_extra": "LLMs draft contracts faster; **auto-anchoring** clauses without human read-through risks **binding erroneous text**.",
        "deep_bullets": [
            "**Evidence packet** — what a third party can verify years later.",
            "**Key ceremonies** — firm-level vs client-level control.",
            "**Jurisdiction** — where data resides and which chain is authoritative.",
        ],
        "composite": "**Composite — discovery hash registry**\n\n- **Situation:** Associate used personal wallet for test anchors.  \n- **Outcome:** **Policy + technical** separation of test/prod; training module outline.",
        "resources_extra": [],
        "touchpoint_hint": "Hash registries, escrow contracts, firm-managed wallets, B2B networks",
        "expert_roles": [
            ("LW", "Legal tech lead", "**Evidence and workflow** alignment."),
            ("PS", "Professional networks", "**Consortium** governance."),
        ],
    },
    {
        "slug": "education-research-credentials",
        "file": "education-research-credentials.md",
        "catalog_id": "education-research-credentials",
        "title": "Education, research & credentials",
        "description": "Micro-credentials, diplomas, open science, and grant traceability on ledgers.",
        "hero_title": "Issue credentials that verify everywhere—and revoke safely",
        "hero_lead": "**Diplomas, badges, and research artifacts** benefit from **portable verification**, but **revocation, privacy, and vendor changes** are hard. Tekvo helps institutions **design credential stacks**, **review issuer contracts**, and **plan wallet experiences** for students and researchers.",
        "rows": [
            (
                "Revocation and expiry",
                "Stale credentials mislead employers.",
                "**Status lists** and **rotation**.",
            ),
            (
                "Student privacy",
                "Transcripts are sensitive.",
                "**Selective disclosure** patterns.",
            ),
            (
                "Vendor churn",
                "Universities outlive startups.",
                "**Portable did methods** and export.",
            ),
            (
                "Research integrity",
                "Preprint anchors can be gamed.",
                "**Timestamp vs content** binding.",
            ),
        ],
        "cards": [
            (
                "Issuer infrastructure",
                "**Keys**, **HSM**, and **batch issuance**.",
            ),
            (
                "Verifier integrations",
                "**Employer and government** APIs.",
            ),
            (
                "Grants and reproducibility",
                "**Funding flows** and **artifact** registries.",
            ),
        ],
        "ai_extra": "AI-generated coursework complicates integrity; on-chain badges need **issuer policy** on what they attest.",
        "deep_bullets": [
            "**Lifecycle** — issuance, suspension, revocation, reissuance.",
            "**Wallet recovery** — student self-sovereignty vs help desk reality.",
            "**Open science** — what metadata is public vs aggregated.",
        ],
        "composite": "**Composite — national micro-credential wallet**\n\n- **Situation:** Multiple issuers on one chain contract.  \n- **Outcome:** **Role isolation** and **schema migration** plan before semester scale.",
        "resources_extra": [
            "**External** — [Verifiable Credentials (W3C)](https://www.w3.org/TR/vc-data-model/).",
        ],
        "touchpoint_hint": "Issuer contracts, wallet SDKs, status services, LMS integrations",
        "expert_roles": [
            ("ED", "Education sector lead", "**Registrar and IT** alignment."),
            ("RS", "Research infrastructure", "**Open science** tooling."),
        ],
    },
]


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    out = root / "docs" / "industry"
    out.mkdir(parents=True, exist_ok=True)
    for meta in INDUSTRIES:
        path = out / meta["file"]
        path.write_text(page(meta), encoding="utf-8")
        print("wrote", path.relative_to(root))


if __name__ == "__main__":
    main()
