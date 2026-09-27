# name = "Sarmila Nepali"
# age = 27
# print(f"\033[95m hi this is {name} and i am {age} years old \033[0m")

# \033[ is the escape sequence, the number + m applies the color, and \033[0m resets it.

print("\033[91m[FATAL ERROR] API connection dropped!\033[0m")     # 91: Bright Red for critical failures
print("\033[92m[SUCCESS] AI Model finished training.\033[0m")     # 92: Bright Green for success
print("\033[93m[WARNING] Server memory is getting low.\033[0m")   # 93: Bright Yellow for warnings
print("\033[96m[INFO] User 'Gorkha' logged in.\033[0m")           # 96: Bright Cyan for general info

for code in range(91, 98):
    print(f"\033[{code}mThis is bright color code {code}\033[0m")

for code in range(31,37):
     print(f"\033[{code}mThis is dim color code {code}\033[0m")
