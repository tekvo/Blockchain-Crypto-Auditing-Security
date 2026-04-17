---
title: Blockchain and smart contract best practices
description: Secure design and operations — OWASP Smart Contract Top 10, ConsenSys patterns, SDLC checkpoints for Ethereum contracts — Tekvo.
---

# Blockchain and smart contract best practices

This page ties together **design-time**, **implementation-time**, and **operational** practices. **[Smart contract attacks](smart-contract-attacks.md)** lists vulnerability classes; **[Web3 security tools](web3-security-tools.md)** maps automation and formal tooling.

## Canonical developer guides

- **[Smart contract best practices (ConsenSys)](https://consensys.github.io/smart-contract-best-practices/)** — patterns for access control, external calls, token standards, and upgrades; actively maintained.
- **[Solidity security considerations](https://docs.soliditylang.org/en/latest/security-considerations.html)** — language- and EVM-specific pitfalls straight from the compiler team.

## OWASP Smart Contract Security (structured risk lists)

The **[OWASP Smart Contract Top 10](https://owasp.org/www-project-smart-contract-top-10/)** project publishes a ranked list of contract risks with detailed pages per category. The live **[2026 Top 10](https://scs.owasp.org/sctop10/)** currently emphasizes (among others):

1. Access control flaws  
2. Business logic errors  
3. Price oracle manipulation  
4. Flash loan–facilitated exploit chains  
5. Missing input validation  
6. Unchecked external calls  
7. Arithmetic / rounding issues  
8. Reentrancy  
9. Integer overflow / underflow on unsafe paths  
10. Proxy and upgradeability mistakes  

Use these as **checklist headings** during design review, not as a substitute for threat modeling.

**Beyond the contract:** the **[OWASP Top 15: Web3 Attack Vectors](https://scs.owasp.org/sctop10/Web3-Attack-Vectors-Top15/)** covers wallets, bridges, RPC, MEV-adjacent issues, and other system-level surfaces — useful when your “smart contract” sits inside a larger product.

Additional OWASP SCS resources:

- **[SCWE](https://scs.owasp.org/SCWE/)** — weakness enumeration aligned to smart contracts.  
- **[OWASP SCS checklists](https://scs.owasp.org/checklists/)** — practitioner checklists.

## Secure development lifecycle (SDLC) for Web3

| Phase | Practices |
| --- | --- |
| **Requirements** | Explicit invariants (who can mint, pause, upgrade; economic bounds). Document trust assumptions on oracles, bridges, and governance. |
| **Design** | Principle of least privilege; separation of roles; timelocks on sensitive parameter changes; fail-safe defaults (paused state clearly defined). |
| **Implementation** | Pin Solidity/compiler; minimal `delegatecall` surface; consistent checks-effects-interactions; no `tx.origin` for auth; safe ERC-20 handling (return values, fee-on-transfer). |
| **Testing** | Unit + integration + **property / invariant** tests (Foundry, Echidna, Medusa); fork tests against mainnet state where oracles/AMM matter. |
| **Review** | Internal pass using [Audit roadmap](audit-roadmap.md); static analysis in CI; differential review for upgrade diffs. |
| **Deploy** | Verified source; constructor args documented; multisig deployer; monitor events post-deploy. |
| **Operate** | Incident runbooks; optional circuit breakers with transparent policy; bug bounty aligned to scope. |

## Operational and key security

- **Multisig and timelocks** for admin; document **who** can invoke **what**, and user-visible delay before destructive actions.  
- **Key rotation** after personnel changes; separate **deploy** keys from **treasury** keys.  
- **Dependency hygiene**: lock npm/yarn/pnpm; review GitHub Actions and third-party CI secrets.  
- **Upgrade discipline**: storage layout checks (OpenZeppelin Upgrades), initializer vs constructor, no self-destruct on library proxies.

## Standards and reference architectures

- **[OpenZeppelin Contracts](https://docs.openzeppelin.com/contracts/)** — audited building blocks (access control, tokens, utils).  
- **[EIP documentation](https://eips.ethereum.org/)** — interop and behavior for tokens, account abstraction, and governance when you implement or integrate EIPs.

---

When reviewing a specific protocol, always ask: *What is the smallest set of keys or signatures that could steal user funds or change verification rules?* If that set is one hot key with no delay, the design is carrying concentrated operational risk even if the Solidity is clean.
