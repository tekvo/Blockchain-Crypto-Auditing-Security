---
title: Smart contract attacks and vulnerability classes
description: Solidity and EVM vulnerability classes — reentrancy, oracles, delegatecall, gas — with links to official docs and research — Tekvo.
---

# Smart contract attacks and vulnerability classes

Reference list of common **Solidity / EVM** pitfalls, with links to official docs, research, and write-ups. **[Blockchain best practices](blockchain-best-practices.md)** collects defensive design patterns alongside this reference.

A **ranked, maintained taxonomy** aligned with recent incidents is the **[OWASP Smart Contract Top 10](https://owasp.org/www-project-smart-contract-top-10/)** and the live **[2026 entries](https://scs.owasp.org/sctop10/)** (access control, business logic, oracle manipulation, flash-loan chains, proxies, and related classes). This Tekvo page stays a **curated grab-bag of primary sources and deep notes** on specific classes (reentrancy, `delegatecall`, gas quirks, and academic papers).

Many production exploits chain several issues—for example **oracle manipulation** or **rounding errors** amplified by a **flash loan** in one transaction. **End-to-end state** across external calls—not only single-function logic—carries most of the risk signal in review.

## Solidity security pitfalls, considerations and recommendations
https://docs.soliditylang.org/en/v0.8.0/security-considerations.html

## Solidity Known Bug List:
https://github.com/ethereum/solidity/blob/develop/docs/bugs.json

## Other Bug list:
https://www.researchgate.net/publication/334908571_Defects_and_Vulnerabilities_in_Smart_Contracts_a_Classification_using_the_NIST_Bugs_Framework

https://github.com/sigp/solidity-security-blog#visibility

## Re-entrancy: 
A reentrancy attack occurs when a function makes an external call to another untrusted contract. Then the untrusted contract makes a recursive call back to the original function in an attempt to drain funds. Find the best practices here
eg: https://hackernoon.com/hack-solidity-reentrancy-attack



## Timestamp Dependence: 
The timestamp dependency vulnerability exists when a smart contract uses the block timestamp as part of the conditions to perform a critical operation (e.g., sending ether) or as the source of entropy to generate random numbers. In a distributed system like blockchain, the miner has the freedom to set the timestamp of a block within a short time interval less than 900 seconds [24]. However, if a smart contract transfers ether based on timestamp, an attacker can manipulate block timestamps to exploit the vulnerability

## Gas Limit and Loops : 
Solidity uses Gas to fuel each transaction on the Ethereum network. Each piece of code costs the user some gas to execute their transaction.
This can prove troublesome if the loops are infinite, as this will cause the transactions to execute till the point the user runs out of Gas, and then the function would fail, producing improper and erroneous results.


## DoS with Block Gas Limit
## Block Stuffing
The Anatomy of a Block Stuffing Attack 
https://medium.com/hackernoon/the-anatomy-of-a-block-stuffing-attack-a488698732ae

## Unbounded Operations

## Transaction-Ordering Dependence

## Insecure function: Use of tx.origin

## Exception Disorder. 
https://personal.ntu.edu.sg/yi_li/files/Wang2019VUL.pdf
https://arxiv.org/ftp/arxiv/papers/1807/1807.03932.pdf
The Exception disorder is due to the fact that Solidity is inconsistent in terms of exception handling, which is dependent on the way contracts call each other. When a contract calls the function of another, it may fail due to different types of exceptions. When such an exception occurs, the handling mechanism is determined by how the calls are made. Given a chain of nested calls where each call is a direct call to the function of a contract, when exception occurs, all the transactions will be reverted (including ether transfer). However, for a chain of nested calls where at least one call is made through low-level call methods on address (address.call(), address.delegatecall(), or address.send()), the rollback of the transaction will only stop at the calling function and return false. From that point, no other side effect can be reverted and no throw will be propagated. Such inconsistencies in terms of exception handling will make the calling contracts unaware of the errors happened during execution

## Gasless send: 
https://arxiv.org/ftp/arxiv/papers/1807/1807.03932.pdf
The gasless send vulnerability is due to the fact that when using send the recipient contract’s fallback function will be invoked but with a fixed gas stipend as determined by the EVM. Usually, the gas limit for the fallback function is 2300 when the amount sent is nonzero. As a result, if the recipient contract has an expensive fallback function, the sender of the ether will get an out of gas exception. If such exception is not checked and propagated appropriately, a malicious sender can keep ether wrongfully while seemingly innocent.

## Balance equality: 
The research paper shows that it is possible to send Ethers to contract even if you rejected Ethers in the fallback function of your contract.
The attacker can execute `selfdestruct` on some contract with the address of your contract. This will send ETH to your contract without invoking the fallback function.
Let's understand this with the help of a contract. In this, the victim contract has implemented a fallback function to reject ether, so the developer of the victim contract assumes no one can send ETH to the contract.
But I can write an Attack contract with a selfdestruct function, where I will pass the address of the victim contract. This will allow me to send Ethers to victim contract. The reason being in case of self destruct, fallback function is not executed.

pragma solidity 0.5.1; contract Victim{ function() external payable { revert(); } function getEthBalance() public view returns (uint){ return address(this).balance; } } contract Attack { function pay() public payable { } function getEthBalance() public view returns (uint){ return address(this).balance; } function kill(address payable victim) public { selfdestruct(victim); } }

How can greater-than or less-than balance checks prevent misuse of `selfdestruct` funding?
That depends entirely on business logic: you should **never** assume that no one can force-send ETH to your contract.


## Byte array

## Transfer forwards all gas: 
As you can see in the withdraw function, it calls payee.sendValue(payment);. The sendValue function is declared in the Address library. And as we can see, it sends the balance using the .call function.
Based on the documentation, the .call function forwards all the gas to the recipient. This is ideal in case a recipient is also a contract that wants to run some other logic and this way it does not run out of gas.
As you can also see from the documentation, the .transfer and .send function only forward 2300 gas, which is enough to receive ether, but not enough to do more complex operations while receiving the ether, like modifying the state of the recipient contract.
That's why it says that it is forwarding all the gas to the recipient, because it's sending the eth using the .call function instead of the .send or .transfer functions.
The gas that is not used by the recipient is returned to the sender contract, and the gas that it does not use is then refunded to the original sender. This way, previous senders can continue doing more operations.
Documentation:
https://docs.soliditylang.org/en/latest/units-and-global-variables.html?highlight=address%20initial#members-of-address-types

## Address library:
https://github.com/OpenZeppelin/openzeppelin-contracts/blob/c1d6e39aab042a38a90f618c614a298522851f7b/contracts/utils/Address.sol#L60



## ERC20 API violation

## Malicious libraries

## Compiler version not fixed

## Redundant fallback function

## Send instead of transfer

## Style guide violation

## Unchecked external call

## Unchecked math

## Stack size limit

## Integer Overflow and Underflow: 
Smart contracts primarily operate upon arithmetic operations, e.g., manipulating participants’ balances. However, these data are usually strongly typed, and thus their arithmetic operations are susceptible to integer overflow/underflow.

## Unsafe type inference 

## Implicit visibility level

## Oracle Manipulation 
Manipulation of external data providers and potential solutions to oracle security issues.

## Delegate call return value
https://arxiv.org/ftp/arxiv/papers/1807/1807.03932.pdf
The delegate call is identical to a message call except that the code at the target address is executed in the context of the calling contract. This means that a contract can dynamically load code from a different address at runtime while the storage still refers to the calling contract. This is the way to implement the “library” feature in Solidity for reusing code. However, when the argument of the delegate call is set as msg.data, an attacker can craft the msg.data with the signature of a function so that the attacker can make the victim contract to call whatever function it provides. This is exemplified by the outbreaks of the first round of parity wallet vulnerability. As shown in Table 1, at line 6 the Wallet contract contains a delegatecall with msg.data as its parameter. This makes an attacker can call any public function of _walletLibrary with the data of Wallet. So, the attacker calls the initWallet function (defined at line 10) of the _walletLibrary smart contract and become the owner the wallet contract. Finally, he can send the ether of the wallet to his own address to finish the attack. This attack has led to $30 million loss to the parity wallet users. Table 1. Dangerous Delegate Call in Parity Wallet Contract 1 contract Wallet{ 2 function() payable { //fallback function 3 if (msg.value > 0) 4 Deposit(msg.sender, msg.value); 5 else if (msg.data.length > 0) 6 _walletLibrary.delegatecall(msg.data); 7 } 8 } 9 contract WalletLibrary { 10 function initWallet(address[] _owners, uint _required, uint _daylimit) { 11 initDaylimit(_daylimit); 12 initMultiowned(_owners, _required); 13 } 14 }

## Freezing Ether: 
https://arxiv.org/ftp/arxiv/papers/1807/1807.03932.pdf
Another type of vulnerable contract is the freezing ether contract. These contracts can receive ether and can send ether to other addresses via delegatecall. However, they themselves contain no functions to send ether to other address. In another word, they purely rely on the code of other contracts (via delegatecall) to send ether. When the contracts providing the ether manipulation code performs suicide or self-destruct operation, the calling contract has no way to send out ether and all its ether is frozen. The second round of attack on Parity wallet vulnerability is just because many wallet contracts can only rely on the parity library to manipulate their ether. When the parity library was changed to a contract through initialization and then killed by the hacker. All the ether within the wallets contracts relying on the parity library is frozen.



