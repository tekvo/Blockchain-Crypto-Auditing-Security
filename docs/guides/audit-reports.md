# Audit reports

Public audit reports help you learn how firms structure findings, severity, and remediation guidance.

## Where to read real reports

- **[QuillAudit public reports (GitHub)](https://github.com/Quillhash/QuillAudit_Reports)**  
- **[OpenZeppelin audits (GitHub)](https://github.com/OpenZeppelin/openzeppelin-contracts/tree/master/audits)** — reports shipped alongside the library they reviewed (good examples of formatting and severity).  
- **[Trail of Bits public reports](https://github.com/trailofbits/publications/tree/master/reviews)** — mix of blockchain and traditional security reviews.  
- **[ConsenSys Diligence reports](https://consensys.io/diligence/audits/)** — browse by protocol; useful for DeFi- and upgrade-heavy scopes.  
- **[Code4rena reports](https://code4rena.com/reports)** — competitive findings; great volume of **individual bugs** with PoCs (quality varies; read critically).

When reading reports, note **scope**, **commit hash or release**, **methodology**, and whether issues were **fixed or acknowledged**.

## How to read a report like a reviewer

1. **Scope box** — unscoped files, periphery contracts, and off-chain bots are often where post-audit incidents occur.  
2. **Threat model** — what did auditors assume about admins, oracles, and economic actors?  
3. **Centralization / operational findings** — severities differ by firm, but “admin can rug” is a business risk as much as a code risk.  
4. **Remediation diff** — single-line fixes can miss adjacent variants; compare **before/after** invariants, not only the patched line.

Treat audits as **time-bounded snapshots**: upgrades after the report date are not covered unless a **re-audit** or incremental review says so.
