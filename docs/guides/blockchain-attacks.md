# Types of blockchain attacks

This note groups common attack surfaces into **network**, **wallet**, **smart contract**, **transaction verification**, and **mining pool** categories. Use it as a map; follow the dedicated smart-contract guide for Solidity-specific classes.

## 1. Blockchain network attacks
    - Distributed denial of service 
    - Transaction malleability attacks
    - Timejacking
    - Routing attacks ( Partition & delay attacks)
    - Sybil attacks ( double-spending attacks )
    - Eclipse attacks
    - Long range attacks on proof of stake networks
      1. Simple — A naive implementation of the proof of stake protocol, when nodes don’t check block timestamps
      2. Posterior corruption — An attempt to mint more blocks than the main chain in a given time frame
      3. Stake bleeding — Copying a transaction from the honestly maintained blockchain to a private blockchain maintained by the attacker

## 2. User wallet attacks
    - Phishing
    - Dictionary attacks
    - Vulnerable signatures
    - Flawed key generation
    - Attacks on cold wallets
    - Attacks on hot wallets
    
## 3. [Smart contract attacks](smart-contract-attacks.md)
    - Vulnerabilities in contract source code
    - Vulnerabilities in virtual machines
        1. Immutable defects
        2. Cryptocurrency lost in transfer
        3. Bugs in access control 
        4. Short address attack
    
## 4. Transaction verification mechanism attacks
    - Double-spending 
    - Finney attacks
    - Race attacks
    - Vector76
    - Alternative history attacks
    - 51% or majority attacks
    
## 5. Mining pool attacks
    - Selfish mining/ block withholding
    - Fork after withholding