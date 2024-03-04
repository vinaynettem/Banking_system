class GenerateStatementUseCase:
    def generate_account_statement(self, account_id):
        account = account_repository.find_account_by_id(account_id)

        # Generate account statement string with transaction details (simplified)
        statement = f"Account Statement for Account ID: {account_id}\n"
        statement += f"Current Balance: {account.get_balance()}\n"
        # Add more details based on transactions (not implemented in this simplified version)

        return statement
