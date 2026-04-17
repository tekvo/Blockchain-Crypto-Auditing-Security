---
title: Code samples
description: Guided Solidity tour — Context, Pausable, and AccessControl patterns with explanations and copyable snippets — Tekvo.
---

# Code samples

Solidity in this repository lives under **`codes/`** at the project root. For **every** `.sol` file with explanation and full copyable source, use the **[Code library](code/index.md)** (Examples, Interfaces & security, Utils). This page is a **shorter guided tour** of three important modules only.

The site theme provides a **clipboard** control on code blocks to copy the displayed snippet.

Treat all examples as **educational only**, not production deployments.

---

## `Context` — execution context abstraction

`Context` wraps `msg.sender` and `msg.data` behind `_msgSender()` and `_msgData()`. That pattern matters when you later add **meta-transactions** or **account abstraction**: callers are not always the EOA that signed the outer transaction, so reading `msg.sender` directly in many places makes upgrades harder.

**What to notice:** thin base contract, both helpers marked `internal view virtual` so subclasses can override behavior.

```solidity linenums="1" title="codes/utils/Context.sol"
--8<-- "codes/utils/Context.sol"
```

**Audit angle:** any `onlyOwner`-style check should use `_msgSender()` (via `Context`) if the rest of the codebase standardizes on it—grep for raw `msg.sender` vs `_msgSender()` for consistency.

---

## `Pausable` — emergency stop pattern

`Pausable` keeps a boolean `_paused`, exposes `whenNotPaused` / `whenPaused` modifiers, and internal `_pause` / `_unpause` for inheriting contracts. Common for tokens or vaults where an admin may halt transfers during an incident.

**What to notice:** modifiers `require` on state; internal pause/unpause emit events and flip the flag only when allowed.

```solidity linenums="1" title="codes/interfaces/security/Pausable.sol"
--8<-- "codes/interfaces/security/Pausable.sol"
```

**Audit angle:** who can call code paths that invoke `_pause` / `_unpause`? Centralized pause without timelock or multisig is a **liveness and trust** concern; also confirm no path lets users withdraw while others are blocked unfairly (policy, not just code shape).

---

## `AccessControl` — roles and `onlyRole` (excerpt)

This slice shows the **`RoleData` struct**, the **`DEFAULT_ADMIN_ROLE`** sentinel, the **`onlyRole`** modifier, and **`hasRole`**. The full contract in the repo adds `grantRole`, `revokeRole`, `_setRoleAdmin`, and revert formatting auditors often grep for.

**What to notice:** roles are `bytes32` keys; membership is a nested mapping; the modifier delegates to `_checkRole` (see full file for revert data).

```solidity linenums="49" title="codes/Examples/AccessControl.sol (lines 49–86)"
--8<-- "codes/Examples/AccessControl.sol:49:86"
```

**Audit angle:** `DEFAULT_ADMIN_ROLE` is self-administering—compromising one admin key can rotate all roles. Enumerate all `grantRole` / `renounceRole` entrypoints and whether **timelocks** or **multisig** protect admin actions.

---

## See also

| Need | Page |
|------|------|
| Full listing of all `codes/` files + copy | [Code library overview](code/index.md) |
| Example contracts only | [Examples](code/examples.md) |
| Interfaces & security mixins | [Interfaces & security](code/interfaces.md) |
| Utils & libraries | [Utils](code/utils.md) |

Clone the repo for tests, diffs, and imports beyond what the site embeds.
