# Blockchain, crypto, and smart contract security

Curated notes and references for **blockchain security**, **smart contract auditing**, and **due diligence** on tokens and protocols. The `codes/` folder holds Solidity interfaces and small examples you can study alongside the guides.

## Contents

| Topic | File |
|--------|------|
| Network, wallet, and verification-layer attacks | [001 Type of Blockchain Attacks.md](./001%20Type%20of%20Blockchain%20Attacks.md) |
| Smart contract vulnerability classes and references | [002 Smart contract attacks.md](./002%20Smart%20contract%20attacks.md) |
| Secure development practices | [003 Blockchain Best Practices.md](./003%20Blockchain%20Best%20Practices.md) |
| Example audit reports | [004 Audit Reports.md](./004%20Audit%20Reports.md) |
| Tools, platforms, and bug frameworks | [005 Web3 Security Tools, Platforms and Frameworks.md](./005%20Web3%20Security%20Tools%2C%20Platforms%20and%20Frameworks.md) |
| EVM internals and low-level work | [006 Working with EVM Low level coding.md](./006%20Working%20with%20EVM%20Low%20level%20coding.md) |
| Internal audit checklist and roadmap | [007 Roadmap for Smart Contract Audit.md](./007%20Roadmap%20for%20Smart%20Contract%20Audit.md) |
| Token screening before investing | [008 Check before investing in crypto tokens.md](./008%20Check%20before%20investing%20in%20crypto%20tokens.md) |
| Secureum resources | [012 Secureum.md](./012%20Secureum.md) |

## Suggested reading order

1. **001** — Threat landscape at the chain, wallet, and contract layers.  
2. **002** + **003** — Contract bugs paired with defensive patterns.  
3. **005** — Tooling and formal methods pointers.  
4. **006** — EVM perspective when reviewing bytecode or gas behavior.  
5. **007** — Practical internal audit checklist before external review.  
6. **008** + **004** — Token due diligence and how professional reports are structured.  
7. **012** — Broader Web3 and Eth2 security reading from Secureum.

## Code samples

Solidity under [`codes/`](./codes/) includes ERC20-related examples, access control, pausable patterns, and utilities (e.g. `SafeMath`, `EnumerableSet`). Treat them as **educational snippets**, not production deployments.

## Disclaimer

All information (tools, links, articles, text, images, and code) is provided **for educational purposes only**. It is compiled from public sources. You are solely responsible for how you use this material and for any decisions you make; the authors and contributors are not liable for your actions.
