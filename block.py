# block.py
# This file defines what a Block looks like in the blockchain.
# Every block stores an index, timestamp, transactions, a previous hash,
# a nonce for Proof-of-Work, and its own hash.

import hashlib
import json
import time
from dataclasses import dataclass, field
from transcation import Transaction

@dataclass
class Block:
    index: int
    timestamp: float
    transactions: list
    previous_hash: str
    nonce: int = 0
    hash: str = field(init=False)

    def __post_init__(self):
        # When a block is created, we immediately compute its hash.
        self.hash = self.compute_hash()

    def compute_hash(self):
        #Creates a SHA-256 hash of the block contents.
        block_data = {
            "index": self.index,
            "timestamp": self.timestamp,
            "transactions": [t.to_dict() for t in self.transactions],
            "previous_hash": self.previous_hash,
            "nonce": self.nonce
        }
        block_string = json.dumps(block_data, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()
