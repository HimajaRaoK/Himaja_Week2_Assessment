'''2. Design a `BankAccount` class with `deposit()` and `withdraw()` methods. 
Implement logic to prevent overdraft.'''

class BankAccount():
    def __init__(self,balance=0):
        self.balance=balance

    def deposit(self,total_amount):
        self.balance=self.balance+total_amount
        print(f"After deposit, balance is {self.balance} rs")

    def withdraw(self,total_amount):
        if (total_amount<=self.balance):
            self.balance=self.balance-total_amount
            print(f"After withdraw, balance is {self.balance} rs")
        else:
            print("No balance, try again")

    def current_balance(self):
        print(f"Current balance is {self.balance} rs")

bank=BankAccount()

while True:
    print("Select from the following:")
    print("1.Deposit")
    print("2.Withdraw")
    print("3.Check balance")
    print("4.Exit")
    choice=input("Enter your choice: ")

    if choice=='1':  
        amount=int(input("Enter amount to deposit: rs"))
        bank.deposit(amount)
    elif choice=='2':  
        amount=int(input("Enter amount to withdraw: rs"))
        bank.withdraw(amount)
    elif choice=='3':  
        print(bank.current_balance())  
    elif choice=='4': 
        print("Exiting.....")
        break
    else:
        print("Invalid, try again.")
              
    

