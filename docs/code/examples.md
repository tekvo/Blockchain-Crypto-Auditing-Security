# Example contracts (`codes/Examples/`)

Educational **concrete contracts** built from the interfaces and utils in this repo—mostly OpenZeppelin v4.5–style patterns. Use the copy control on each block to grab the full file.

[← Back to code library overview](index.md)

---

## `ERC20.sol`

{: #erc20sol }

**Path:** `codes/Examples/ERC20.sol`

Standard **ERC20** implementation: balances, allowances, `transfer` / `transferFrom`, mint/burn hooks as internal `_mint` / `_burn`, and metadata (`name`, `symbol`, `decimals`). Reverts on failure (no `bool` return false). Good reference when auditing token accounting, approvals, and hook ordering.

```solidity linenums="1" title="codes/Examples/ERC20.sol"
--8<-- "codes/Examples/ERC20.sol"
```

---

## `AccessControl.sol`

{: #accesscontrolsol }

**Path:** `codes/Examples/AccessControl.sol`

**Role-based access control**: `bytes32` roles, `DEFAULT_ADMIN_ROLE`, `grantRole` / `revokeRole`, and the `onlyRole` modifier. Study admin rotation, `_setRoleAdmin`, and how revert strings expose missing roles during reviews.

```solidity linenums="1" title="codes/Examples/AccessControl.sol"
--8<-- "codes/Examples/AccessControl.sol"
```

---

## `AccessControlEnumerable.sol`

{: #accesscontrolenumerablesol }

**Path:** `codes/Examples/AccessControlEnumerable.sol`

Extends `AccessControl` with **on-chain enumeration** of role members via `EnumerableSet`. Useful for UIs and audits that need “who holds role X?”—mind gas and consistency when iterating across blocks.

```solidity linenums="1" title="codes/Examples/AccessControlEnumerable.sol"
--8<-- "codes/Examples/AccessControlEnumerable.sol"
```

---

## `ERC20PresetMinterPauser.sol`

{: #erc20presetminterpausersol }

**Path:** `codes/Examples/ERC20PresetMinterPauser.sol`

**Preset token**: ERC20 + burn + **minter** and **pauser** roles (wired through `AccessControlEnumerable`, `ERC20Burnable`, `ERC20Pausable`). Deployer gets admin, minter, and pauser. Classic surface for audits: role grants, pause liveness, and mint caps in subclasses.

```solidity linenums="1" title="codes/Examples/ERC20PresetMinterPauser.sol"
--8<-- "codes/Examples/ERC20PresetMinterPauser.sol"
```

---

## `UseERC20PresetMinterPauser.sol`

{: #useerc20presetminterpausersol }

**Path:** `codes/Examples/UseERC20PresetMinterPauser.sol`

Minimal **subclass** of `ERC20PresetMinterPauser`: constructor passes name/symbol, and **admin-only** helpers grant `MINTER_ROLE` and `PAUSER_ROLE`. Demonstrates how privileged roles can be exposed beyond the preset defaults.

```solidity linenums="1" title="codes/Examples/UseERC20PresetMinterPauser.sol"
--8<-- "codes/Examples/UseERC20PresetMinterPauser.sol"
```
