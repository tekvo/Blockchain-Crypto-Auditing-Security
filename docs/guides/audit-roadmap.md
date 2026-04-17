# Roadmap for auditing smart contracts (Tekvo / internal review)

A practical checklist for an **initial internal security pass** before engaging a third-party auditor. Adapt items to your protocol’s threat model and scope.

## 1. Documentation

Solid documentation is the baseline for any review.

- Business requirements documentation  
- Technical requirements documentation  
- Expected behavior versus implemented logic (traceability)  
- Test cases (automate where possible) and a log of executed tests  
- Test results from testnets or staging deployments  
- Version control for requirements and design so code changes stay aligned  
- Implementation strictly follows the agreed specification  

## 2. Automated and static analysis

- Run suitable auditing / analysis tools (example workflow): [bscheck](https://bscheck.eu/)  
- Integrate findings with manual review; tools do not replace human judgment  

## 3. Bug and abuse-case testing

- Harmful or unexpected transactions: ordering dependencies, stack limits, arithmetic issues, and related classes in [Types of blockchain attacks](blockchain-attacks.md) and [Smart contract attacks](smart-contract-attacks.md)  
- Token minting: supply caps, roles, timelocks, and upgrade paths  
- If **pause** exists: model rug-pull and liveness scenarios (who can pause, for how long, and what user funds are affected)  
- **Delegatecall**, proxies, and third-party calls: storage layout, implementation upgrades, and trust boundaries  
- Factory pattern correctness: [Cloning Solidity smart contracts (LogRocket)](https://blog.logrocket.com/cloning-solidity-smart-contracts-factory-pattern/)  
- **Migrator** patterns: high historical abuse; see [RugDoc on migrators](https://rugdoc.io/education/migrator/)  
- **Renounce ownership** ([EIP-173](https://eips.ethereum.org/EIPS/eip-173)): intentional, documented, and not masking centralized control elsewhere  
- No hidden **emergency withdraw** that drains user principal outside stated policy  
- **Locktime** / vesting where token economics require it  
- No unexpected **liquidity removal** or admin-only drains from pools users rely on  
- No opaque **strategy change** functions that reallocate user assets without consent  
- **Burn** mechanics: not used to hide supply manipulation or block sells  
- Each function’s behavior matches its name, NatSpec, and external documentation  
- Input validation under a Byzantine / adversarial model  
- Dependencies on external contracts, libraries, and **oracles** (staleness, manipulation, fallback behavior)  

## 4. Tax, trading, and gas

- Avoid redundant external calls; optimize hot paths for gas without sacrificing safety  
- **Honeypot** checks: users can sell under realistic conditions on the target DEX/router  
- Buy and sell paths both work as advertised  
- If taxes exist, keep them within your project’s stated bounds (many communities treat ~5% as a rough ceiling for “reasonable” swap taxes—verify against your own policy)  

## 5. Distribution and concentration

- Locked or burned supply aligned with whitepaper (often teams aim for a large majority locked or verifiably burned—tune thresholds to your model)  
- Top holders: monitor concentration among the largest 5–10 wallets versus circulating supply  

## 6. Third-party audit (industry standard)

After internal review, engage a reputable firm for a **scoped** audit, then track remediation and **re-review** of critical fixes.
