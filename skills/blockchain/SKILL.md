---
description: "Use this skill whenever the user asks to verify Ethereum/EVM address activity (MetaMask/Sepolia testnet tasks), check whether an address interacted with a contract, verify NFT mints, token transfers, contract calls, or to cross-check a class list of addresses against on-chain activity on any EVM chain (Ethereum, Sepolia, Polygon, Base, Arbitrum, Optimism, etc.). Especially trigger when grading assignments that involve wallet addresses, Etherscan/Alchemy checks, or “has the student sent/received transactions?”."
version: 1.0.0
---

# Blockchain (EVM) Verification Skill

This skill is a **practical playbook** for querying Ethereum and EVM-compatible chains for:
- address activity / first transaction time
- “did this address send a transaction?”
- “did this address interact with a given contract?”
- NFT mint verification
- bulk verification of many student addresses

## Default approach (important)

### Prefer Alchemy free-tier method
On Alchemy free tier, `eth_getLogs` is severely range-limited. For most “did they do something?” checks, **use**:
- **`alchemy_getAssetTransfers`** (fast, indexed, includes timestamps)

### Always do a single-test query first
Before running a loop over a whole class list:
1) test one known address
2) confirm response shape and timestamps
3) only then scale up

## Inputs you should clarify
When the user asks a blockchain check, clarify:
1) **chain/network** (Sepolia vs mainnet etc.)
2) **what counts as success** (any tx? a tx to friend? contract interaction? NFT mint?)
3) **deadline / due time** (for on-time/late decisions)

## Address hygiene rules
- Valid EVM address format: `0x` + **40 hex chars**.
- Normalize comparisons using `.lower()`.
- For web3.py calls, convert to checksum with `Web3.to_checksum_address()`.
- **EOA vs Contract**: Definitive check is `eth_getCode` (code == `0x` → EOA).

---

## Pattern A — Fetch outgoing transfers (most grading tasks)
Use this to confirm the student actually used the wallet (sent a tx).

```python
import requests

RPC_URL = f"https://eth-sepolia.g.alchemy.com/v2/{ALCHEMY_KEY}"

def outgoing_transfers(address, max_count=100):
    payload = {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "alchemy_getAssetTransfers",
      "params": [{
        "fromAddress": address,
        "category": ["external", "erc20", "erc721", "erc1155"],
        "withMetadata": True,
        "order": "asc",
        "maxCount": hex(max_count),
      }]
    }
    j = requests.post(RPC_URL, json=payload, timeout=30).json()
    return j.get("result", {}).get("transfers", [])
```

**What to record in a mark sheet** (recommended columns):
- Address valid? (Y/N)
- Outgoing tx count (sample)
- First outgoing tx timestamp (UTC)
- First tx hash

---

## Pattern B — Check “sent to friend/classmate”
If the assignment expects “send ETH to a friend”, you can use the class address sheet itself as the friend list:
1) Build `class_addr_set = {addr.lower() ...}` from the sheet
2) For each student’s outgoing transfers, check if any `to` is in that set (excluding self)

---

## Pattern C — Contract interaction (address ↔ contract)
Use `alchemy_getAssetTransfers` filtered to a `toAddress` (or `fromAddress` depending on direction).

```python
payload = {
  "jsonrpc": "2.0",
  "id": 1,
  "method": "alchemy_getAssetTransfers",
  "params": [{
    "fromAddress": STUDENT,
    "toAddress": CONTRACT,
    "category": ["external", "erc20", "erc721", "erc1155"],
    "withMetadata": True,
    "order": "asc",
    "maxCount": "0x3e8"
  }]
}
```

---

## Pattern D — NFT mint verification (free-tier friendly)
Mint = transfer where `from` is the null address.

```python
payload = {
  "jsonrpc": "2.0",
  "id": 1,
  "method": "alchemy_getAssetTransfers",
  "params": [{
    "contractAddresses": [NFT_CONTRACT],
    "fromAddress": "0x0000000000000000000000000000000000000000",
    "category": ["erc721"],
    "withMetadata": True,
    "order": "asc",
    "maxCount": "0x3e8"
  }]
}
```

---

## Timeliness note (important limitation)
- **Google Sheets API does not provide per-cell edit timestamps**.
- If the task requires “submitted before due time”, use a **proxy** such as:
  - first outgoing transaction time on-chain
  - first interaction with target contract

Always state this clearly in the rubric.

---

## Rate limits & safety
- Add small sleeps (e.g., 100–200ms) between requests in loops.
- Save intermediate JSON (so you can resume after failures).
- Never hardcode private keys.
- Never treat “address exists” as “student did activity”: addresses exist even if unused.
