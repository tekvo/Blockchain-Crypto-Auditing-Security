# Utils (`codes/utils/`)

Shared **helpers and libraries** used by the example contracts. Each entry is the full file—copy from the block as needed.

[← Back to code library overview](index.md)

---

## `Context.sol`

{: #contextsol }

**Path:** `codes/utils/Context.sol`

Abstract **execution context**: `_msgSender()` and `_msgData()` wrap `msg.sender` / `msg.data` for compatibility with meta-tx patterns. Prefer this indirection in shared base classes so you can override sender resolution in one place.

```solidity linenums="1" title="codes/utils/Context.sol"
--8<-- "codes/utils/Context.sol"
```

---

## `SafeMath.sol`

{: #safemathsol }

**Path:** `codes/utils/operators/SafeMath.sol`

**Overflow-checked** arithmetic for older Solidity semantics; on modern `^0.8` the language has built-in checks, but this module is still useful when reading legacy codebases or porting patterns. Compare gas and revert behavior against native math.

```solidity linenums="1" title="codes/utils/operators/SafeMath.sol"
--8<-- "codes/utils/operators/SafeMath.sol"
```

---

## `String.sol`

{: #stringsol }

**Path:** `codes/utils/datatypes/String.sol`

String utilities (e.g. conversion helpers) used by access-control revert messages and similar. Inspect for **gas** on hot paths if you adapt this into production-style code.

```solidity linenums="1" title="codes/utils/datatypes/String.sol"
--8<-- "codes/utils/datatypes/String.sol"
```

---

## `EnumerableSet.sol`

{: #enumerablesetsol }

**Path:** `codes/utils/structs/EnumerableSet.sol`

Library for **add/remove/contains** on sets, including `AddressSet`, used by enumerable access control. Core to on-chain role enumeration—audit iteration limits and whether callers can grief admins with growth.

```solidity linenums="1" title="codes/utils/structs/EnumerableSet.sol"
--8<-- "codes/utils/structs/EnumerableSet.sol"
```
