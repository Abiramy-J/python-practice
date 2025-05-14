def deposit(balance,amount):
    if amount>0:
        balance+=amount
        print("successful deposit!,your current balance: $",balance)
        return balance

    else:
        print("amount must be greater than 0")
        return balance

#====git testin===


def withdraw(balance,amount):
    if amount<=balance:
        balance-=amount
        print("successful withdrawal!,Remaining balance: $",balance)
    elif amount>balance:
        print("insufficient fund")
    else:
        print("Error;withdrawal amount must be greater than 0")


def main():
    balance=50000
    while True:
        print("1.deposit")
        print("2.withdraw")
        print("3.show balance")
        print("4.exit")

        choice=input("choose the option 1 to 4:")
        
        if choice=="1":
            try:
                amount=float(input("Enter the deposit amount:"))
                balance=deposit(balance,amount)
            except ValueError:
                print("invalid deposit amount")
        elif choice=="2":
            try:
                amount=float(input("Enter the withdrawal amount:"))
                balance=withdraw(balance,amount)
            except ValueError:
                print("invalid withdrawal amount")

        elif choice=="3":
            print("Now ur current balance: $",balance)
        elif choice=="4":
            print("Thank you,for using our sevice.")
            break
        else:
            print("invalid option,choose option 1 to 5")


main()

                




