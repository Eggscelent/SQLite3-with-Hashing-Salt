import sys
from functions import create_account, login
def index():
    while True:
        print("\n----- DB Login Test -----")

        options = {
            'a': create_account,
            'b': login,
            'c': sys.exit
        }

        menu_value = input("""
        a: Create Account
        b: Login
        c: Exit

        Please enter your choice [A-C]: """).lower()

        selected_option = options.get(menu_value)

        if selected_option:
            selected_option()
        else:
            print("Invalid choice. Please enter A, B, or C.")


if __name__ == "__main__":
    index()