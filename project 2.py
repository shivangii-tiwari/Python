class ATM:
    def __init__(self):
        self.balance = 0
        self.transacition = []
    def display_balance(self):
        print("enter your current balance: ",self.balance)

    def deposit(self):
        amount = int(input("enter the amount you want to deposite: "))
        self.balance += amount
        self.tansaction.append(f"deposite: {amount}")
        print ("amount deposite sucessfully")

    def withdraw(self):
        amount = int(input("enter the amount to withdraw: "))
        if amount > self.balance:
            print("insufficent balance")
        else:
            self.balance -= amount
            self.transcation.append(f"withdraw: {amount}")
            print("collect your amount")

        def show_transcaitions(self):
            print("transcation history: ")
            if len(self.transcations) == 0:
                print("no transcation yet")
            else:
                for transcations in self.transcations:
                    print("trancations occur")


# creating object
atm = ATM()
while True:
    print("1. check balance")
    print("2. deposit")
    print("3. withdraw")
    print("4. transcation history")
    print("5. exit")

    choice = input("enter your choice: ")
    if choice == "1":
        atm.display_balance()
    elif choice == "2":
        atm.deposit()
    elif choice == "3":
        atm.withdraw()
    elif choice == "4":
        atm.show_transcations()
    elif choice == "5":
        print("Thankyou for using atm")
        break
    else:
        print("invalid choice")

    