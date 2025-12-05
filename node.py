# node.py
# A Node represents a user in the network.
# Each node keeps its own blockchain and a list of pending transactions.

import uuid
from blockchain import Blockchain
from transcation import Transaction
from block import Block

class Node:
    def __init__(self, name, difficulty=4):
        self.name = name
        self.id = str(uuid.uuid4())
        self.blockchain = Blockchain(difficulty=difficulty)
        self.pending_transactions = []

    def create_transaction(self, sender, recipient, amount):
    # Adds a valid transaction to the node's pending list.
        tx = Transaction(sender, recipient, amount)   # <-- THIS MUST EXIST

        if not tx.is_valid():
            print(f"[{self.name}] Invalid transaction.")
            return False

        self.pending_transactions.append(tx)
        print(f"[{self.name}] Transaction created: {tx}")
        return True

    def mine_pending_transactions(self):
    #Mines all pending transactions into a new block.
        if not self.pending_transactions:
            print(f"[{self.name}] No transactions to mine.")
            return None

        new_block = self.blockchain.add_block(self.pending_transactions)
        print(f"[{self.name}] Mined block #{new_block.index}")
        self.pending_transactions = []
        return new_block

    def receive_block(self, block):
       
        # Accept a block mined by someone else.
        # Only accepts it if it fits on top of the chain AND is valid.
        
        if block.previous_hash != self.blockchain.last_block.hash:
            print(f"[{self.name}] Rejected block (bad previous hash).")
            return False

        self.blockchain.chain.append(block)

        if not self.blockchain.is_chain_valid():
            self.blockchain.chain.pop()
            print(f"[{self.name}] Rejected block (chain invalid).")
            return False

        print(f"[{self.name}] Accepted block #{block.index}")
        return True
