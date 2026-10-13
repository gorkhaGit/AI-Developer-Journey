# funtions are reusable peiced of codes that run when you call them to run
# """ for example : " print()"
# another funtion is "input()" which lets you user to input the valuer
# example:
# name = input("what is your name?")
# print(f"Hello {name}")

# another one " int()"
# int() converts string and boolean  and numbers into integer value
# print(int(True))
# print(int(False))
# print(int(2.232))
# print(int("42"))

# def funtion le afule chayeko custom funtion bnaunu maddat gracha,,
# def lekhne tespxi afule chayeko  function  lekhne ani """
# next linema code afule chaheyko code lekkne"

# def name():
#     print("gorkha nepali")

# def calculate_sum(a ,b):
#     return a + b

# my_summ = calculate_sum(3 ,1)
# # print(my_sum)
# def create_greetin(username):
#     return f"Welcome to your ai dashboard, {username}!"
# user_message = create_greetin("Sarmila nepali")
# print(user_message)

# def calculate_sum(a,b):
#     return( a + b)
# my_sum = calculate_sum(3 ,1)
# print(my_sum)
# app_name = "Gorkha Ai"
# def generate_text(prompt):
#     api_key = "secret key 123"
#     response = f"Sending '{prompt}' to {app_name} using {api_key}"
#     return response
# # This works because we call the function properly:
# print(generate_text("Write a Python script"))

# # This works because app_name is Global:
# print(app_name)

# # This will CRASH. api_key is Local. Python doesn't know what it is out here.
# print(api_key)
available_eggs = 1
available_flour = 2
available_sugar = 3

def check_kitchen_stock():
    total_items = available_eggs + available_flour + available_sugar
    print(f'The kitchen has {total_items} total items:')
    print(f'- {available_eggs} eggs')
    print(f'- {available_flour} flour')
    print(f'- {available_sugar} sugar')

check_kitchen_stock()

def use_eggs(available_eggs, eggs_to_use):
    if eggs_to_use > available_eggs:
        print('The kitchen does not have enough eggs.')
        return available_eggs

    print(f'{eggs_to_use} egg(s) used out of {available_eggs} available.')
    return available_eggs - eggs_to_use

use_eggs(available_eggs, 1)
print(available_eggs)

def make_fried_egg(available_eggs):
    has_enough_eggs = available_eggs >= 1

    if has_enough_eggs:
        available_eggs = use_eggs(available_eggs, 1)
        print('Made a fried egg. Yummy!')
    else:
        print('Could not make a fried egg. Not enough eggs!')

    return available_eggs