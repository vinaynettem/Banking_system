class MakeTransactionUseCase:
    def make_transaction(self, account_id, amount, transaction_type):
        account = account_repository.find_account_by_id(account_id)

        if transaction_type == 'deposit':
            account.deposit(amount)
        elif transaction_type == 'withdraw':
            account.withdraw(amount)

        # Save the updated account back to the repository (not implemented in this simplified version)
        account_repository.save_account(account)
