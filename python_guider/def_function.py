# 1. This is our GLOBAL variable. 
# user_role = "Guest"

# def check_access(user_role):
#     # 2. Because the parameter is also named 'user_role', it SHADOWS the global one.
#     # Python will only use whatever you pass into this function.
#     print(f"Granting access level: {user_role}")

# # Let's pass in "Admin"
# check_access("Admin")  
# # Output: Granting access level: Admin

# # 3. If we print the global variable down here, it hasn't changed.
# print(f"The global role is still: {user_role}") 
# # Output: The global role is still: Guest

# 1. We create our global variable
global_role = "Guest"

def check_access(user_role):
    # 3. Inside the function, let's look at what the local reference points to
    print(f"Inside function, local 'user_role' points to memory ID: {id(user_role)}")

# 2. Let's check the memory address of our global variable
print(f"Outside function, 'global_role' is at memory ID: {id(global_role)}")

# 4. Now we pass the global variable into the function
check_access(global_role)