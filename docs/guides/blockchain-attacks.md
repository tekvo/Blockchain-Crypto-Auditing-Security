---
title: Types of blockchain attacks
description: Attack surfaces across networks, wallets, smart contracts, MEV, bridges, and consensus — threat-model outline with mitigations — Tekvo.
---

# Types of blockchain attacks

This page maps common attack surfaces across the **network**, **wallet**, **smart contract**, **transaction layer**, **mining / consensus**, and **cross-chain** stack. It is organized as a **threat-model outline**: each class ties to **who controls the failure point**, **what invariant breaks**, and **what evidence typically appears on-chain or in infrastructure**. Network- and wallet-layer rows align with **operational controls** (monitoring, key ceremony, incident playbooks) as well as technical mitigations. For Solidity-specific classes and references, see [Smart contract attacks](smart-contract-attacks.md).

## 1. Blockchain network attacks {: #network-attacks }

| Attack | What breaks | Mitigations (directional) |
| --- | --- | --- |
| **Distributed denial of service (DoS)** | Availability: peers or RPC endpoints cannot keep up with load. | Rate limits, diverse RPC providers, client tuning, network-level filtering where you operate nodes. |
| **Transaction malleability** | Transaction IDs can change without invalidating signatures (historically important for Bitcoin-style chains). | Use non-malleable sighash schemes; do not rely on `txid` before confirmation where malleability exists. |
| **Timejacking** | Node time skew influences acceptance of blocks or difficulty. | NTP discipline, peer diversity, client defaults that bound clock assumptions. |
| **Routing / partition attacks** | Adversary isolates a node or subnet from honest network view (BGP, ISP, P2P layer). | Multiple upstream peers, geographically diverse bootstraps, VPN/tunneling for critical validators (ops tradeoffs). |
| **Sybil / eclipse** | Attacker surrounds victim with dishonest peers or Sybil identities to feed false chain tips or censor txs. | Peer diversity, anchor connections, checkpoint awareness; for light clients, verify against multiple sources. |
| **Long-range (PoS)** | Old keys or weak subjectivity assumptions let an alternate finalized history be argued. | Weak subjectivity checkpoints, client diversity, social consensus on canonical deployments. |

Further reading: Ethereum’s [proof-of-stake attack and defense](https://ethereum.org/en/developers/docs/consensus-mechanisms/pos/attack-and-defense/) (high-level consensus threats).

## 2. User wallet and key-management attacks {: #wallet-attacks }

| Attack | What breaks | Mitigations (directional) |
| --- | --- | --- |
| **Phishing / fake dApps** | User signs malicious payloads or sends funds to attacker-controlled addresses. | Hardware wallets, transaction preview tools, address blocklists, bookmark official URLs, verify contract on explorer. |
| **Seed / keystore theft** | Confidentiality of signing keys. | Cold storage, multisig, social recovery with clear trust model, minimal clipboard exposure, malware hygiene. |
| **Flawed key generation** | Predictable or biased nonces / keys. | Use audited libraries; never “roll your own” RNG; verify device firmware. |
| **Hot wallet compromise** | Single online key signs high-value txs. | Segregate hot vs cold; use HSM or MPC for orgs; policy limits and human approvals. |
| **Supply-chain on dev machines** | Malicious `node_modules`, fake compiler, or IDE plugin alters bytecode or deployer key. | Lockfiles, dependency review, reproducible builds, separate deploy keys, CI signing gates. |

See also [Blockchain best practices](blockchain-best-practices.md) for secure SDLC and operations.

## 3. Smart contract and VM-layer attacks {: #contract-vm-attacks }

- **Source-level bugs**: reentrancy, access control, oracle manipulation, upgrade mistakes — see [Smart contract attacks](smart-contract-attacks.md).
- **VM / bytecode assumptions**: incorrect `delegatecall` targets, opcode behavior across forks, compiler bugs — track [Solidity known bugs](https://github.com/ethereum/solidity/blob/develop/docs/bugs.json) and pin compiler versions intentionally.

OWASP’s current [Smart Contract Top 10](https://owasp.org/www-project-smart-contract-top-10/) (and the live [2026 list](https://scs.owasp.org/sctop10/)) aligns well with incident data: access control, business logic, oracles, flash-loan chains, and proxy/upgrade issues dominate many post-2020 exploits.

## 4. Transaction verification and ordering attacks {: #tx-ordering-attacks }

| Attack | What breaks | Mitigations (directional) |
| --- | --- | --- |
| **Double-spend / race** | Conflicting spends before sufficient confirmations. | Wait for confirmations; for merchants, use payment processors with risk policies. |
| **Finney attack** | Miner includes a conflicting spend in their own block. | Same as above; reduce trust in zero-conf acceptance. |
| **51% / majority** | Attacker has enough hash or stake to reorganize recent history. | Deep confirmations; monitor hashrate / stake distribution; chain-specific finality gadgets. |
| **MEV (ordering)** | Block builders reorder, insert, or sandwich txs for profit; users get worse execution. | Private RPC / bundles, slippage limits, protocol-level fair ordering or encrypted mempools (tradeoffs apply). |

**Scope note — MEV:** **Arbitrage**, **liquidations**, and **just-in-time liquidity** are often benign or welfare-improving; the security lens is **unfair extraction** versus **stated user expectations**. Protocol documentation normally states whether users should expect **builder-level ordering** behavior.

## 5. Mining and staking pool attacks {: #mining-pool-attacks }

| Attack | What breaks | Mitigations (directional) |
| --- | --- | --- |
| **Selfish mining / block withholding** | Honest miners’ expected revenue; potentially chain liveness perception. | Protocol design and reward variance; pool reputation; detect abnormal orphan patterns. |
| **Pool operator trust** | Centralized payout or work distribution can steal or censor. | Stratum/V2 improvements, smaller pool share targets, solo staking where feasible. |

## 6. Cross-chain bridges and messaging {: #bridge-attacks }

Bridges combine **smart contract risk**, **cryptography / signature verification**, **validator or relayer trust**, and **operations** (upgrades, pauses, key rotation). Recurring failure modes include:

- **Faulty or incomplete message verification** (messages accepted from wrong domain, replay, or stale roots).
- **Upgrade / admin paths** that can change verification logic without user-visible notice.
- **Oracle or liquidity assumptions** on destination chains that a single tx can violate (often chained with flash loans on DeFi).

**User / integrator hygiene:** understand the bridge’s **trust model** (who can pause, who signs, what asset is canonical), prefer **canonical or light-client–style** designs where your threat model allows, use **limits** on first-time flows, and monitor **[L2BEAT](https://l2beat.com/)**-style risk disclosures for rollups and bridges.

Further reading: [OWASP Web3 Attack Vectors (Top 15)](https://scs.owasp.org/sctop10/Web3-Attack-Vectors-Top15/) (includes areas beyond a single contract, e.g. bridge and wallet ecosystems).

## 7. Social engineering and governance {: #social-governance-attacks }

- **Fake “support”**, **Discord / Twitter hijacks**, and **malicious airdrop claims** push users to sign `setApprovalForAll` or malicious `permit` messages.
- **Governance capture** (token vote buying, flash-loan votes, low turnout) changes protocol parameters or upgrades implementations.

Mitigations: clear comms channels, timelocks with **exit windows**, guardian roles with constrained scope, and **post-mortems** published after incidents.

---

**Legacy bullet index** (quick scan): network DoS, malleability, timejacking, routing/partition, Sybil, eclipse, long-range PoS; wallet phishing, dictionary attacks, bad signatures/keygen, cold/hot wallet attacks; contract/VM issues (immutable defects, lost-in-transfer bugs, access control, short address); verification-layer double-spend, Finney, race, vector76, alt history, 51%; pool selfish mining and fork-after-withholding.
