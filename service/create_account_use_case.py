from Domain.account import Account
from Domain.customer import Customer

class CreateAccountUseCase:
    def create_account(self, customer_id, name, email, phone_number):
        # Assume account_id and account_number are generated elsewhere (for simplicity)
        account_id = generate_account_id()
        account_number = generate_account_number()

        customer = Customer(customer_id, name, email, phone_number)
        account = Account(account_id, customer_id, account_number, 0)

        # Save the account to the repository (not implemented in this simplified version)
        account_repository.save_account(account)

        return account
