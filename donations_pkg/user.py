def login(database, username, password):
    if username in database.keys() and database[username] == password:
        print("welcome", username)
        return username
    elif username in database.keys() and database[username] != password:
        print("Wrong Password ")
        return ""
    else:
        print("User name not found")
        return ""


def register(database, username, password):

    if len(username) > 10:
        print("The Max username is 10 Characters")
        return ""
    if len(password) <= 5:
        print("Password  min is 5 characteres")
        return ""

    if username.lower() in database.keys():
        print("Username already registered!")
        return ""
    else:
        print("Username has been registered!")
        return username
