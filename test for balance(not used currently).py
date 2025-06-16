import csv

file_path = 'user.csv'

name = 'Sultan'
balance = 100

def add_balance(name):

    list_user = []

    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for item in reader:
            list_user.append(item)
    
    for users in list_user:
        if name in users:
            list_users_index = list_user.index(users)
            user_index = list_user[list_users_index]
            balance_index = user_index[2]
            balance_index = int(balance_index)
            new_balance = balance_index + balance

    user_index.insert(2, new_balance)
    user_index.pop(3)
    list_user.pop(list_users_index)
    list_user.append(user_index)

add_balance(name)