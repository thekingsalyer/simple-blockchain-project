Simple Blockchain System (Python) is an implementation of a basic blockchain that was created for educational purposes, as well as to show how the underlying aspects of a blockchain actually operate, 
such as transactions and functionalities of blocks, hashing, proof of work mechanism, a multitude of nodes that are acting as "distributed", and block synchronization, across a small network.

For this system, multiple nodes, or users, have their own copy of the blockchain stored locally. When one node mines a block and broadcasts it to other nodes in the network,
those nodes will validate and append the newly mined block to their respective copies of the blockchain. This emulates how real distributed networks maintain consensus on a shared state of affairs
How to Run

Clone or download the project.

Open a terminal inside the project folder.

Run the main demo script:

python run.py


If your Python command is python3, use:

python3 run.py

Expected Output

Nodes get registered to the network

Users create transactions

Nodes mine blocks using Proof-of-Work

Mined blocks get broadcast to all nodes

Each node accepts valid blocks and updates its chain

All nodes end with the same chain length

Final chain validity check prints True for each node

Example:

Chain lengths:
Alice: 3
Bob:   3
Carol: 3

Chain valid?:
Alice: True
Bob:   True
Carol: True- the validity of all transactions recorded within a block.
