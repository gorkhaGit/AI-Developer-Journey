# using built in datetime module

# from datetime import date
# birth_year = 1996
# age = date.today().year - birth_year
# print(age)

# from datetime import date
# graduation_year = 2016
# year_count = date.today().year - graduation_year
# print(year_count)

# third practise

# from datetime import date
# marriage_year = 2018
# past_year = date.today().year - marriage_year
# print(past_year)

# input exercise

from datetime import date
birthday = input(f"what is your birthyear?")
age = date.today().year - int(birthday)
print(f" you are exactly : {age} years old, Gorkha!!")

# from datetime import date( important to remember)