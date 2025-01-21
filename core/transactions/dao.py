from core.transactions.types import InsertTransactionModel



class TransactionModelAccess:
    SUBDIR = "/transactions"

    def __init__(self):
        pass

    def get_transactions(self):
        ...

    def create_transactions(self, transactions: list[InsertTransactionModel]):
        ...

    def update_transactions(self):
        ...
