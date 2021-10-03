# hello admin 

usernames = ['admin', 'user1', 'user2', 'user3', 'user4']

for username in usernames: 
    if username == 'admin':
        print("Hello Admin, would you like a status report?")
    else:
        print(f"Hello {username.title()}, thank you for logging in again.")


#no users in the list

usernames = []

if usernames:
    for username in usernames:
        print(f"Hello {username.title()}, thank you for logging in again.")
else:
    print("We need to find some users!")


# checking usernames

current_users = ['userone', 'usertwo', 'userthree', 'userfour', 'userfive']
current_users = [user.lower() for user in current_users] 

new_users = ['usereight', 'usersix', 'userthree', 'userone']
new_users = [user.lower() for user in new_users]

    #covert lists to lower case using list comprehension

for new_user in new_users:
    if new_user in current_users:
        print(f"Sorry, {new_user} is not available please choose another username.")
    else:
        print(f"Congratulations, {new_user} your username is available.")

# ordinal numbers 

ordinal_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print("\nOrdinal Numbers:")

for ordinal_number in ordinal_numbers:
    if ordinal_number == 1:
        print(f"{ordinal_number}st")
    elif ordinal_number == 2:
        print(f"{ordinal_number}nd")
    elif ordinal_number == 3:
        print(f"{ordinal_number}rd")
    else:
        print(f"{ordinal_number}th")