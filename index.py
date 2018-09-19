films = {
    "Race 3": [12, 25, 200],
    "Ant-Man": [16, 25, 300],
    "Deadpool 2": [18, 18, 180],
    "Infinity-War": [12, 29, 400],
    "Stranger Things 3": [3, 10, 350],
}


users = {

    1: {
        "username": "admin",
        "password": "admin"
    },
   2: {
        "username": "varsha",
        "password": "varsha062"
    },
    3: {
        "username": "sakshi",
        "password": "memelover"
    },
    4: {
        "username": "jhanvi",
        "password": "pizzalover"
    },
    5: {
        "username": "aastha",
        "password": "asslover"
    },
}

print(users.items())
def addUser():
    i=6
    users[i] = {}
    users[i]["username"] = input("Enter username ")
    users[i]["password"] = input("Enter password")

addUser()




# temp = []
# for i in range(1,41):
#     if i % 10 == 0:
#         temp.append(i)rac
#         print('\n', temp)
#         temp.clear()
#     else:
#         temp.append(i)


def movieChoice():
    for key in films.keys():
        print(key)


movieChoice()
choice = input("\nEnter Movie name: ").strip().title()

# Selection of movie
if choice in films:
    age = int(input("Enter yor age:\n"))

    # verifying age
    if age >= films[choice][0]:
        print("Great,  price of a ticket is {}  .".format(films[choice][2]))
        choice2 = input("Do you want proceed further to buy thickets ?(y/n) ").strip().lower()

        # proceeding further for purchasing
        if choice2 == 'y':

            # asking amount of tickets
            amount = int(input("Enter number of tickets you want to buy :\n"))
            if amount <= films[choice][1]:

                # calculating total amount of bill
                billAmount = amount * films[choice][2]
                print("Your total bill for {} thickets is {}".format(amount, billAmount))
                # If ticket are less available tickets
            elif amount > films[choice][1]:
                print("Sorry we have only {} tickets available".format(films[choice][1]))
        elif choice2 == 'n':
            print("Thank you for visiting us !")

    elif age < films[choice][0]:
        print("Sorry , you are too yong to watch this movie.")
elif choice is not films:
    print("Sorry, this movie is not available please try again.")
