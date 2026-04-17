---
title: Web3 security tools
description: Smart contract security tooling — Slither, fuzzing, formal verification, on-chain investigation, and bug frameworks — Tekvo.
---

# Web3 security tools, platforms, and frameworks

Collections and references for **static analysis**, **testing and fuzzing**, **formal methods**, **monitoring**, **on-chain investigation**, and **bug taxonomies**. Tools complement manual review; they do not replace it.

## Static analysis and linters

| Tool | Role |
| --- | --- |
| **[Slither](https://github.com/crytic/slither)** (Trail of Bits) | Fast static analysis, detectors, printers, inheritance/graph views; common in CI. |
| **[solhint](https://github.com/protofire/solhint)** | Solidity linter with security-oriented rules. |
| **[Semgrep](https://semgrep.dev/)** + community Solidity rules | Pattern matching across repos; good for org-specific forbidden APIs. |
| **[Solidity SMTChecker](https://docs.soliditylang.org/en/latest/smtchecker.html)** | Built-in model checking for assertions and some safety properties. |

## Fuzzing, property testing, and symbolic execution

| Tool | Role |
| --- | --- |
| **[Echidna](https://github.com/crytic/echidna)** | Property-based fuzzer for Solidity; invariant testing. |
| **[Medusa](https://github.com/crytic/medusa)** | Multi-contract fuzzing / parallel exploration (Crytic ecosystem). |
| **[Foundry](https://book.getfoundry.sh/forge/invariant-testing)** (`forge test`) | Unit tests, fuzz, and **invariant** tests against local or forked state. |
| **[Halmos](https://github.com/a16z/halmos)** | Symbolic bounded model checker for Solidity (good for focused properties). |

## Formal verification (contracts)

| Tool / service | Role |
| --- | --- |
| **[Certora Prover](https://www.certora.com/)** | Specification language and prover used widely in DeFi audits. |
| **[KEVM / Kontrol](https://github.com/runtimeverification)** | K-framework–based semantics and verification (steep learning curve, high assurance). |

Formal work stays grounded in explicit **specifications** (what must always be true). See [Formal verification (Solidity docs)](https://docs.soliditylang.org/en/latest/security-considerations.html#formal-verification).

## Bytecode, diffing, and execution exploration

| Resource | Role |
| --- | --- |
| **[hevm](https://github.com/ethereum/hevm)** | Symbolic execution for EVM bytecode; useful for equivalence checks. |
| **[evm-codes](https://www.evm.codes/)** | Opcode reference for manual bytecode review. |
| **[Surya](https://github.com/ConsenSys/surya)** | Visualization of inheritance and call graphs from Solidity. |

## Monitoring, automation, and incident response

| Platform | Role |
| --- | --- |
| **[OpenZeppelin Defender](https://docs.openzeppelin.com/defender/)** | Autotasks, monitors, upgrades workflow (vendor SaaS). |
| **[Forta](https://forta.org/)** | Decentralized monitoring network; community and custom detection bots. |
| **[Tenderly](https://docs.tenderly.co/)** | Simulations, alerts, and debugging (SaaS). |

## Security tools and curated lists

### Quillhash

- **[Web3 security tools (GitHub)](https://github.com/Quillhash/Web3-Security-Tools)** — diagrams and categorized tool lists.

### Resources listed by Secureum

- **[Smart contract security resources](https://secureum.substack.com/p/smart-contract-security-resources)**

## On-chain investigation

- **[On-chain investigations tools list](https://github.com/OffcierCia/On-Chain-Investigations-Tools-List)**  
- **[Investigation flow (Mirror)](https://officercia.mirror.xyz/BFzv17UwH6QG4q711NAljtSiP8eKR17daLjTdmAgbHw)**  
- **[Independent investigators (Vice)](https://www.vice.com/en/article/xgd9zw/meet-the-blockchain-detectives-who-track-cryptos-hackers-and-scammers)**

## Smart contract bug frameworks

### Bugs Framework (BF)

The BF includes rigorous definitions and static attributes of bug classes along with their related dynamic properties.

- **[Bugs Framework paper](https://www.atlantis-press.com/journals/ijndc/125913574/view)**

### SmartBugs

- **[SmartBugs: a framework for analyzing Solidity smart contracts](https://arxiv.org/abs/2007.04771)** — extensible framework and benchmark datasets.

### OWASP

- **[OWASP SCWE](https://scs.owasp.org/SCWE/)** — smart contract weakness enumeration.  
- **[OWASP Smart Contract Top 10](https://owasp.org/www-project-smart-contract-top-10/)** — awareness document aligned with recent incidents.

## Datasets and learning from incidents

- **[DeFiHackLabs](https://github.com/SunWeb3Sec/DeFiHackLabs)** — reproduced PoCs for many public incidents (educational; verify against primary sources).  
- **[rekt.news](https://rekt.news/)** — narrative post-mortems (editorial; cross-check on-chain data).

Use datasets to train internal **red-team scenarios**, not as legal or financial advice.
