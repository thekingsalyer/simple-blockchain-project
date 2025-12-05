# run_demo.py
# This script creates a small blockchain network with three nodes
# and demonstrates:
# - making transactions
# - mining
# - broadcasting blocks
# - validating the chain

from node import Node
from network import Network

def main():
    network = Network()

    # Create three users
    alice = Node("Alice")
    bob = Node("Bob")
    carol = Node("Carol")

    network.register_node(alice)
    network.register_node(bob)
    network.register_node(carol)

    # Create some transactions
    alice.create_transaction("Alice", "Bob", 10)
    alice.create_transaction("Bob", "Carol", 5)
    bob.create_transaction("Carol", "Alice", 2)

    # Alice mines her transactions
    block1 = alice.mine_pending_transactions()
    if block1:
        network.broadcast_block(alice, block1)

    # Bob mines his transactions
    block2 = bob.mine_pending_transactions()
    if block2:
        network.broadcast_block(bob, block2)

    # Check final chain lengths
    print("\nChain lengths:")
    print("Alice:", len(alice.blockchain.chain))
    print("Bob:  ", len(bob.blockchain.chain))
    print("Carol:", len(carol.blockchain.chain))

    # Validate chains
    print("\nChain valid?:")
    print("Alice:", alice.blockchain.is_chain_valid())
    print("Bob:", bob.blockchain.is_chain_valid())
    print("Carol:", carol.blockchain.is_chain_valid())

if __name__ == "__main__":
    main()
