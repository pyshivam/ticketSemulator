# films = {
#     "Race": [12, 25, 200],
#     "Ant-Man": [16, 25, 300],,,
#     "Deadpool": [18, 18, 180],
#     "Infinity-War": [12, 29, 400],
#     "Stranger Things 3": [3, 10, 350],
#     "Game of thorns": [18, 10, 350],
#
# }
# choice = ''
#
# # selection of movie
# def movieChoice():
#     global choice
#     print(" Movies available".upper())
#     print("="*20)
#     for key in films.keys():
#         print(key)
#     print("=" * 20)
#     choice = input("Enter movie name: ").strip().title()
#
# movieChoice()
# if choice in films:
#     age = int(input("Please enter your age: "))
#
#     #Age Verification
#     if age >= films[choice][0]:
#         print("-"*20)
#         #Displying price of selected movie
#         print("Price of a ticket is {}  .".format(films[choice][2]))
#         choice2 = input("Do you want proceed further to buy thickets ?(y/n) ").strip().lower()
#
#         # proceeding further for purchasing
#         if choice2 == 'y':
#
#             # asking amount of tickets
#             amount = int(input("Enter number of tickets you want to buy :\n"))
#             if amount <= films[choice][1]:
#                 # calculating total amount of bill
#                 billAmount = amount * films[choice][2]
#                 print("Your total bill for {} thickets is {}".format(amount, billAmount))
#                 # If ticket are less available tickets
#     else:
#         print("You are not eligible for {}".format(choice))
#         print("Try other movies")
#         movieChoice()
#
# else:
#     print("This movie is not available , try other ")
#     movieChoice()

t=[10,63,95,6,19]
for i in range(1,6):
    for j in t:
        if t[i]>j:
            temp = t[i]
            t[i]=j
            j=temp
            print(t)
