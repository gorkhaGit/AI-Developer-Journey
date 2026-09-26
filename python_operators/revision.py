# number = int(input("enter a number :"))

# if number >= 10 and number <= 50:
#     print("this number in between 10-50")
# else:
#     print("this is number doestnt qualify")

''' operators
arithmetic operators 
math calculations

syntxax  + - / * 
normal , maths

// '''

# print( 6 / 5)

# print( 6 // 5)
# %  = remainder dekhauchaa

# print( 6 % 5)

# print( 2 ** 6)

# print(64 ** 0.5)
# '''
''' ASSIGNMENT OPERATORS'''

# x = 2

# x += 3  #add and asssign
# print(x)

# x -= 5
# print(x)
# x += 6

# print(x + 4)

# assignment operatorsle pailai bhayeko variable to value lai arithmetic operation pxi naya value assign grne kam grcha


''' comprarison operators'''

#  > < >= <= =  == 

# > greater than , < smaller than,
#  == equals to
# != equals to 

# x = 5
# y = 8
# print( x <= y)

# print(x != y)

''' logical operators'''

#  and , or , not

# email = "gorkha7698@gmail.com"
# password = "gorkha123"

# input_gmail = "gorkha7698@gmail.com"
# Password = "Gorkha123"

# access_granted = (input_gmail ==email) and (password == Password)

# print(f"loging succesfull : { access_granted}")


# userId = "gorkha007"
# Pass = "test0123"

# usertyped = input(f"type yout userid ...")
# gopyanumber = input(f"type your password ...")

# login_succesfull = (userId == usertyped) and (Pass == gopyanumber)

# print(f"access : {login_succesfull}")

# x = True
# y  = False
# print(not y)

# real_useid = "sarmila08"
# real_key = "sahana08"

# typed_useid = input(f"Please type your use id :- ")
# typed_key = input(f"now type your key :- ")

# access_granted = (real_useid ==typed_useid) and (real_key == typed_key)

# if access_granted :
#     print(f"Congratulation, come in")
# else :
#     print(f"you are not real user")

# is_banned = True
# if not is_banned:
#     print("welcome!!")
# else:
#     print("WTF!!")
''' membership operators
kunain pni sring wa list ma variable or values exist grcha ki grdain check grcha'''

my_list = [f" a, b , c, d, e"]

user_type = input(f"enter your letter:")

if user_type in my_list:
    print(f"congrats you good to go!!")

if user_type not in my_list :
    print(f"trying again later!!")
    

