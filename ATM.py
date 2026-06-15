class ATM:
    account_holder = ""
    pin = 0
    balance = 0.0
    account_created = False

    def create_account():
        if ATM.account_created:
            print("\nAccount already exists!")
            return

        ATM.account_holder = input("\nEnter Account Person Name: ")

        ATM.pin = int(input("Create a 4-Digit PIN: "))
        ATM.balance = float(input("Enter Initial Deposit Amount: "))

        ATM.account_created = True

        print("\nAccount Created Successfully!")

    def login():
        if not ATM.account_created:
            print("\nPlease create an account first!\n")
            return False

        entered_pin = int(input("\nEnter PIN: "))

        if entered_pin == ATM.pin:
            print("Login Successful!\n")
            return True
        else:
            print("Incorrect PIN!\n")
            return False

    def check_balance():
        print(f"\nCurrent Balance: {ATM.balance}")

    def deposit():
        amount = float(input("\nEnter Deposit Amount: "))

        if amount > 0:
            ATM.balance += amount
            print("Deposited Successfully.\n")
        else:
            print("Invalid Amount!\n")

    def withdraw():
        amount = float(input("\nEnter Withdrawal Amount: "))

        if amount <= 0:
            print("Invalid Amount!\n")
        elif amount > ATM.balance:
            print("Insufficient Balance!\n")
        else:
            ATM.balance -= amount
            print("Withdrawn Successfully.\n")

    def change_pin():
        old_pin = int(input("\nEnter Current PIN: "))

        if old_pin == ATM.pin:
            new_pin = int(input("Enter New PIN: "))
            ATM.pin = new_pin
            print("PIN Changed Successfully!\n")
        else:
            print("Incorrect Current PIN!\n")

    def view_account_details():
        print("\n===== ACCOUNT DETAILS =====\n")
        print(f"Account Holder: {ATM.account_holder}")
        print(f"Available Balance: {ATM.balance}\n")


def main():
    while True:
        print("\n=================================")
        print("       ATM MANAGEMENT SYSTEM")
        print("=================================")
        print("\n1. Create Account")
        print("2. Login")
        print("3. Exit")

        choice = int(input("\nEnter Choice: "))

        if choice == 1:
            ATM.create_account()

        elif choice == 2:
            if ATM.login():
                while True:
                    print("\n========= ATM MENU =========")
                    print("1. Check Balance")
                    print("2. Deposit Money")
                    print("3. Withdraw Money")
                    print("4. Change PIN")
                    print("5. View Account Details")
                    print("6. Logout")
                    atm_choice = int(input("\nEnter Choice: "))

                    if atm_choice == 1:
                        ATM.check_balance()
                    elif atm_choice == 2:
                        ATM.deposit()
                    elif atm_choice == 3:
                        ATM.withdraw()
                    elif atm_choice == 4:
                        ATM.change_pin()
                    elif atm_choice == 5:
                        ATM.view_account_details()
                    elif atm_choice == 6:
                        print("\nLogged Out Successfully!")
                        break
                    else:
                        print("\nInvalid Choice!\n")
        elif choice == 3:
            print("\nThank You For Using ATM!")
            break
        else:
            print("\nInvalid Choice!")


if __name__ == "__main__":
    main()


