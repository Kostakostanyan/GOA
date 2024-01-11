class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid deposit amount. Please enter a positive value.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew ${amount}. New balance: ${self.balance}")
            else:
                print("Insufficient funds. Cannot withdraw more than the available balance.")
        else:
            print("Invalid withdrawal amount. Please enter a positive value.")

    def get_balance(self):
        return self.balance



if __name__ == "__main__":
    
    account = BankAccount(1000)

   
    account.deposit(500)

   
    account.withdraw(200)

    
    account.withdraw(1200)

    
    final_balance = account.get_balance()
    print(f"Final balance: ${final_balance}")