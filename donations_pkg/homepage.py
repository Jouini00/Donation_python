from functools import total_ordering
from unittest.loader import VALID_MODULE_NAME


def show_homepage():
    print("")
    print("========== DonateMe Homepage ==========")
    print("---------------------------------------")
    print("| 1. Login        | 2. Register       |")
    print("---------------------------------------")
    print("| 3. Donate       | 4. Show Donations |")
    print("---------------------------------------")
    print("|               5. Exit               |")
    print("---------------------------------------")


def donate(username):

    donation_amt = input("Enter amount to donate: ")
    try:
        val = float(donation_amt)
        if val < 0:
            print("Sorry, input must be a positive integer, try again")
            return ''
    except ValueError:
        print("Not valid input")
        return ''

    donation_string = (username + " donated $"+str(donation_amt) + ".")
    print("Thank you for your donation!")
    return donation_string


def show_donations(donations, total):
    print("\n--- All Donations ---")

    if donations == []:
        print("Currently, there are no donations.")
    else:
        for amount in donations:
            print(amount)
            index = amount.index("$") + 1
            int_amount = float(amount[index:-1])
            total = int_amount + total
    print("Total = $", total)
