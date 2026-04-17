---
title: Solidity interfaces and security modules
description: Solidity interfaces and security mixins — IERC20, IAccessControl, burn and pause patterns with copyable source — Tekvo.
---

# Interfaces & security modules (`codes/interfaces/`)

**Interfaces** define external APIs for ERC20, access control, introspection, and **security mixins** (burn, pause) used by the examples. Full source in each block—copy with the header **clipboard** control.

[← Back to code library overview](index.md)

---

## `IERC20.sol`

{: #ierc20sol }

**Path:** `codes/interfaces/tokens/ERC20/IERC20.sol`

Canonical **ERC-20** interface: `totalSupply`, `balanceOf`, `transfer`, `allowance`, `approve`, `transferFrom`, and standard events. Compare any token implementation against this surface during audits.

```solidity linenums="1" title="codes/interfaces/tokens/ERC20/IERC20.sol"
--8<-- "codes/interfaces/tokens/ERC20/IERC20.sol"
```

---

## `IERC20Metadata.sol`

{: #ierc20metadatasol }

**Path:** `codes/interfaces/tokens/ERC20/extensions/IERC20Metadata.sol`

Optional **metadata** extension: `name`, `symbol`, `decimals`. Many UIs and explorers assume these exist—flag proxies that omit them or return mutable strings.

```solidity linenums="1" title="codes/interfaces/tokens/ERC20/extensions/IERC20Metadata.sol"
--8<-- "codes/interfaces/tokens/ERC20/extensions/IERC20Metadata.sol"
```

---

## `ERC20Burnable.sol`

{: #erc20burnablesol }

**Path:** `codes/interfaces/tokens/ERC20/security/ERC20Burnable.sol`

**Burn** helpers on top of the local `ERC20` example: `burn` and `burnFrom` (allowance-based). Audit supply changes, fee-on-transfer interactions, and whether burns are user-only or admin-gated in concrete deployments.

```solidity linenums="1" title="codes/interfaces/tokens/ERC20/security/ERC20Burnable.sol"
--8<-- "codes/interfaces/tokens/ERC20/security/ERC20Burnable.sol"
```

---

## `ERC20Pausable.sol`

{: #erc20pausablesol }

**Path:** `codes/interfaces/tokens/ERC20/security/ERC20Pausable.sol`

Combines **ERC20** with **`Pausable`**: `_beforeTokenTransfer` requires `!paused()`. Central for emergency-stop reviews—who can pause, for how long, and what happens to user funds.

```solidity linenums="1" title="codes/interfaces/tokens/ERC20/security/ERC20Pausable.sol"
--8<-- "codes/interfaces/tokens/ERC20/security/ERC20Pausable.sol"
```

---

## `IAccessControl.sol`

{: #iaccesscontrolsol }

**Path:** `codes/interfaces/security/IAccessControl.sol`

**AccessControl** interface: role admin changes, grant/revoke events, `hasRole`, `getRoleAdmin`, and `DEFAULT_ADMIN_ROLE`. Use for ERC-165 discovery and off-chain monitoring of permission changes.

```solidity linenums="1" title="codes/interfaces/security/IAccessControl.sol"
--8<-- "codes/interfaces/security/IAccessControl.sol"
```

---

## `IAccessControlEnumerable.sol`

{: #iaccesscontrolenumerablesol }

**Path:** `codes/interfaces/security/IAccessControlEnumerable.sol`

Extends `IAccessControl` with **`getRoleMember`** / **`getRoleMemberCount`** for enumerating role holders on-chain. The same **`EnumerableSet`** machinery underpins admin-set reasoning and griefing via membership churn.

```solidity linenums="1" title="codes/interfaces/security/IAccessControlEnumerable.sol"
--8<-- "codes/interfaces/security/IAccessControlEnumerable.sol"
```

---

## `Pausable.sol`

{: #pausablesol }

**Path:** `codes/interfaces/security/Pausable.sol`

Reusable **pause** flag, modifiers `whenNotPaused` / `whenPaused`, and internal `_pause` / `_unpause` with events. Imported by `ERC20Pausable` and any contract that needs a global circuit breaker.

```solidity linenums="1" title="codes/interfaces/security/Pausable.sol"
--8<-- "codes/interfaces/security/Pausable.sol"
```

---

## `IERC165.sol`

{: #ierc165sol }

**Path:** `codes/interfaces/introspections/ERC165/IERC165.sol`

**EIP-165** interface: single `supportsInterface(bytes4)` view. Foundation for interface detection in composable systems.

```solidity linenums="1" title="codes/interfaces/introspections/ERC165/IERC165.sol"
--8<-- "codes/interfaces/introspections/ERC165/IERC165.sol"
```

---

## `ERC165.sol`

{: #erc165sol }

**Path:** `codes/interfaces/introspections/ERC165/ERC165.sol`

Minimal **ERC165** base: `supportsInterface` returns true for `IERC165` id; subclasses override to add more ids (as `AccessControl` does for `IAccessControl`).

```solidity linenums="1" title="codes/interfaces/introspections/ERC165/ERC165.sol"
--8<-- "codes/interfaces/introspections/ERC165/ERC165.sol"
```
