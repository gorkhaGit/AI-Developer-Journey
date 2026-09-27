# real_email = "sahana7698@gmail.com"
# user_typed = "Sahana7698@gmail.com"

# # login_access = (real_email == user_typed)
# # print(login_access)

# correct_login = ( real_email == user_typed.lower())
# # print(correct_login)

# #  using .stip()
# bulk_messy = "   my name is gorkha       "
# clear_sentence = bulk_messy.strip()
# print(clear_sentence)

# using.replace()
# raw_filename = " my profile picture.png"
# safe_filename = raw_filename.replace(" ", "_")
# print(f"Original_filename; {raw_filename}")
# print(f"url_ready : {safe_filename}")

# name = "sxntosh"
# print(name.replace("x", "a"))
# name = "sarmila, sahana , sabina, sandhya"
# print(name.split())

# A raw string imported from a simple database or CSV
# db_row = "gorkha-dev,admin,active"

# # We chop the string into a list everywhere there is a comma
# parsed_data = db_row.split(',')

# print(f"Raw String: {db_row}")
# # Notice the square brackets in the output indicating a list[cite: 4]
# print(f"List Array: {parsed_data}") 

# # Because it's now a list, you can grab the exact piece you need using an index
# # print(f"Account Status: {parsed_data[2]}") # Outputs: active

# raw_names = "sarmila,sahana,sandhya,sapana,sabina"
# print(f"individual_name :{raw_names.split(",")}")

# individual_name = ['sarmila', 'sahana', 'sandhya', 'sapana', 'sabina']

# print(f"name_string = {"/".join(individual_name)}")

# name = "sarmila"
# print(name.find("a"))

