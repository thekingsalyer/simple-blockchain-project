# network.py
# This file simulates a very simple in-memory "network" where all
# nodes register and broadcast blocks to each other.

from node import Node

class Network:
    def __init__(self):
        self.nodes = []

    def register_node(self, node):
        self.nodes.append(node)
        print(f"[Network] Node registered: {node.name}")

    def broadcast_block(self, sender, block):
        # Send a mined block to every other node.
        print(f"[Network] Broadcasting block {block.index} from {sender.name}")
        for n in self.nodes:
            if n is not sender:
                n.receive_block(block)
