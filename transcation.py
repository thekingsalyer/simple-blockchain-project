# transaction.py
# This file defines a simple Transaction class.
# A transaction has a sender, a recipient, and an amount.
# For this project, we are not using signatures or wallets.
# Just basic validation to show the idea.

from dataclasses import dataclass

@dataclass
class Transaction:
    sender: str
    recipient: str
    amount: float

    def is_valid(self) -> bool:
        # Basic rules to check if a transaction is valid.
        if not self.sender or not self.recipient:
            return False
        if self.sender == self.recipient:
            return False
        if self.amount <= 0:
            return False
        return True

    def to_dict(self):
        #Makes the transaction easy to convert into JSON later.
        return {
            "sender": self.sender,
            "recipient": self.recipient,
            "amount": self.amount
        }
