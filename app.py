from donations_pkg.homepage import show_homepage, donate, show_donations

from donations_pkg.user import login, register

database = {"admin": "password123"}
donations = []
authorized_user = ""

show_homepage()

if authorized_user == "":
    print(" You must be logged in to donate.")
else:
    print("Logged in as", authorized_user)

while True:
    choice = input("Please select an option ")
    show_homepage()
    if choice == "1":
        username = input("Enter username:  ")
        username = username.lower()
        password = input("Enter password:  ")
        authorized_user = login(database, username, password)

    elif choice == "2":
        username = input("Enter username:  ")
        username = username.lower()
        password = input("Enter password:  ")
        authorized_user = register(database, username, password)
        if authorized_user != "":
            database[username] = password
    elif choice == "3":
        if authorized_user == "":
            print("You are not logged in.")
        else:
            donation_string = donate(authorized_user)
            if donation_string != '':
                donations.append(donation_string)

    elif choice == "4":
        total = 0
        show_donations(donations, total)

    elif choice == "5":
        print("Goodbye")
        break
    else:
        print("Wrong input! Please try again")
