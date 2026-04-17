---
title: EVM low-level coding
description: EVM bytecode, opcodes, gas, delegatecall, and transient storage for security-minded review — Tekvo.
---

# Working with the EVM (low-level view)

Useful material when you need to reason about **bytecode**, **execution traces**, or **gas**, not only Solidity source.

## Introduction: commands, execution, and gas

- [EVM analysis guide (evm-tools)](https://github.com/CoinCulture/evm-tools/blob/master/analysis/guide.md)

## Understanding bytecode

- [Diving into the Ethereum VM (Qtum blog)](https://blog.qtum.org/diving-into-the-ethereum-vm-6e8d5d2f3c30)

For opcode reference and internals, also see the [Ethereum yellow paper](https://ethereum.github.io/yellowpaper/paper.pdf) and [EVM codes in the execution specs](https://www.evm.codes/).

## Security-relevant EVM details (review checklist)

When you are **not** only reading Solidity, these behaviors often explain “mysterious” exploits or gas failures:

- **`delegatecall` context**: callee code runs with **caller storage**, `msg.sender`, and `msg.value` from the **caller** frame. Storage collisions between proxy and implementation are a top source of critical bugs — align with [EIP-1967](https://eips.ethereum.org/EIPS/eip-1967) style slots and documented layout.  
- **`call` vs `staticcall`**: value transfer and state changes require `call`; view-only paths should use `staticcall` so reentrancy and unexpected state writes are harder to sneak in via libraries.  
- **Return data and bubbles**: low-level calls can **return false** instead of reverting; Solidity’s `try/catch` only catches external *reverts*, not all failure modes of raw calls — always check success flags and returned ABI data where relevant.  
- **`selfdestruct` / forced ETH**: ether can be forced to a contract via `selfdestruct` without running the recipient’s receive/fallback — never assume `address(this).balance == 0` means “no one can fund this contract.”  
- **`CREATE2` and init code**: predictable deployment addresses enable **counterfactual** patterns but also **metamorphic** risks if init code can change deployed runtime under adversarial conditions — review factory + init bytecode together.  
- **Transient storage ([EIP-1153](https://eips.ethereum.org/EIPS/eip-1153))**: `TLOAD`/`TSTORE` is **cleared at end of transaction**; it can simplify reentrancy-safe patterns but must not be mistaken for persistent storage across calls in the same tx from unrelated contracts without clear reasoning.  
- **Gas stipends and 63/64 rule**: nested calls and refunds interact with the **call stack depth** and **gas forwarding** rules; denial-of-service via gas griefing often shows up only at bytecode/trace level.

For a guided tour of traces and tooling, keep the [EVM analysis guide (evm-tools)](https://github.com/CoinCulture/evm-tools/blob/master/analysis/guide.md) open next to a failing transaction in your client’s tracer.
