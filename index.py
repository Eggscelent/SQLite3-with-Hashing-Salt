import sys
from termcolor import colored
from colorama import *
from functions import createaccount, login

init()

while True:
    print(colored("\n----- DB Login Test -----", "yellow"))

    menuvalue = input("""
    a: Create Account
    b: Login
    c: Exit

    Please enter your choice [A-C]: """)

    if menuvalue == "A" or menuvalue == "a":
        createaccount()

    if menuvalue == "B" or menuvalue == "b":
        login()

    if menuvalue == "C" or menuvalue == "c":
        print(colored("\nTerminating session...", "red"))

        sys.exit()

    else:
        print("You must only enter a letter from the menu")
        print("Please try again")
