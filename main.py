from infra.account_repository import AccountRepository
from service.create_account_use_case import CreateAccountUseCase
from service.generate_statement_use_case import GenerateStatementUseCase
from service.make_transaction_use_case import MakeTransactionUseCase

# Instantiate necessary objects
create_account_use_case = CreateAccountUseCase()
make_transaction_use_case = MakeTransactionUseCase()
generate_statement_use_case = GenerateStatementUseCase()
account_repository = AccountRepository()

# Example usage
customer_id = "C123"
name = "John Doe"
email = "john.doe@example.com"
phone_number = "123-456-7890"

# Create an account
new_account = create_account_use_case.create_account(customer_id, name, email, phone_number)

# Make a deposit
make_transaction_use_case.make_transaction(new_account.account_id, 100, "deposit")

# Make a withdrawal
make_transaction_use_case.make_transaction(new_account.account_id, 50, "withdraw")

# Generate account statement
statement = generate_statement_use_case.generate_account_statement(new_account.account_id)

# Print the account statement
print(statement)
