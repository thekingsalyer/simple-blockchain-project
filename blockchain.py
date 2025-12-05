# blockchain.py
# This file contains the main Blockchain class.
# It handles creating the chain, adding blocks, mining, and validation.

import time
from block import Block
from transcation import Transaction

class Blockchain:
    def __init__(self, difficulty=4):
        # Difficulty = number of leading zeros required in the hash.
        self.difficulty = difficulty
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
    # Creates a shared genesis block with a fixed timestamp so all nodes match.
        fixed_timestamp = 1700000000  # any fixed number; ensures identical hash

        genesis = Block(
            index=0,
            timestamp=fixed_timestamp,
            transactions=[],
            previous_hash="0"
            )

        mined = self.proof_of_work(genesis)
        self.chain.append(mined)


    @property
    def last_block(self):
        return self.chain[-1]

    def proof_of_work(self, block):
     
        # Simple Proof-of-Work:
        # Keep changing the nonce until the hash starts with N zeros.
      
        target = "0" * self.difficulty

        while True:
            block.hash = block.compute_hash()
            if block.hash.startswith(target):
                return block
            block.nonce += 1

    def add_block(self, transactions):
        #Creates and mines a new block using the given transactions.
        new_block = Block(
            index=len(self.chain),
            timestamp=time.time(),
            transactions=transactions,
            previous_hash=self.last_block.hash
        )
        mined_block = self.proof_of_work(new_block)
        self.chain.append(mined_block)
        return mined_block

    def is_chain_valid(self):
        #Checks the chain to make sure all hashes + links are correct.
        target = "0" * self.difficulty

        for i in range(1, len(self.chain)):
            curr = self.chain[i]
            prev = self.chain[i - 1]

            # Check hash is correct
            if curr.hash != curr.compute_hash():
                return False
            
            # Check link between blocks
            if curr.previous_hash != prev.hash:
                return False

            # Check difficulty
            if not curr.hash.startswith(target):
                return False

        return True
