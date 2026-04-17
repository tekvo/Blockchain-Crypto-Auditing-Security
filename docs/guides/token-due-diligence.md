---
title: Token due diligence
description: Token screening on EVM chains — liquidity, roles, taxes, MEV, and bridge risk before investing — educational, not financial advice — Tekvo.
---

# Checks before investing in crypto tokens

Quick screening ideas for tokens on **BSC**, **Ethereum**, **Polygon**, **Fantom**, and other **EVM-compatible** chains. This is **not** financial advice; use it as a starting checklist and do your own research.

## Automated token screens

- [BSCheck](https://bscheck.eu/) — contract and holder heuristics on several chains  
- [QuillCheck (QuillAudits)](https://quillaudits.com/tools/quillcheck) — additional automated signals  

Treat tool output as **hints**. False positives and false negatives happen; verify on-chain and in the verified source.

## Manual follow-ups

- Read the **verified** contract source (or proxy implementation) on a block explorer  
- Map **mint**, **burn**, **pause**, **blacklist**, **fees**, **owner**, and **upgrade** roles  
- Check **liquidity** lock duration and which address controls the LP tokens  
- Compare **socials** and **official deployments** to avoid impersonation tokens  

### Wrapped, bridged, and “same ticker” risk

- **Bridged assets** inherit the bridge’s trust model; depeg or bridge compromise can make the token worthless even if the ERC-20 code is fine. Prefer understanding **canonical vs wrapped** supply on each chain.  
- **Permit / signature phishing**: attackers trick users into signing allowances for unrelated contracts. Treat unexpected signature prompts as high risk.  
- **Trading / MEV**: thin pools and high default slippage increase **sandwich** and **bad fill** risk; this is not always a “contract bug” but affects realized value — see [transaction ordering and MEV](blockchain-attacks.md#tx-ordering-attacks) in the attacks guide.

Cross-link: [Roadmap for auditing smart contracts](audit-roadmap.md) for patterns auditors often flag. For the full network and bridge map, see [Types of blockchain attacks](blockchain-attacks.md).
