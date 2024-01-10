# The money
money = 0

while True:
    # Questions
    print("[1]  Deposit")
    print("[2]  Withdrawal")
    print("[3]  Balance")
    print("[4]  Exit")
    question = input("Option: ")

    # Deposit
    if question == '1' or question =="deposit" or question == "Deposit":
        print("Deposit")
        deposit_number = int(input("How mutch?: "))

        if deposit_number < 0:
            print("Number greather than 0")

        else:
            money = money + deposit_number
            print("The balance is", money)

    # Withdrawl
    if question == '2' or question == "withdrawal" or question == "Withdrawal":
        print("Withdrawl")
        withdrawl_number = int(input("How mutch: "))
        if withdrawl_number < 0:
            print("Number greather than 0")

        if money < withdrawl_number:
            print("The balance is less than yout withrawl")
        else:
            money = money - withdrawl_number
            print(money)

    # Balance
    if question == '3' or question == "balance" or question == "Balance":
        print("Balance:", money)

    # Exit
    if question == '4' or question == "exit" or question == "Exit":
        break
