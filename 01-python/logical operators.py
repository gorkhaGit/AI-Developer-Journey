# logical operators 
# and or not

# ========================================================
#               BOOLEAN LOGIC TRUTH TABLE
# ========================================================
#
#   X   |   Y   | X and Y | X or Y | not X | not Y 
# --------------------------------------------------------
# True  | True  |  True   |  True  | False | False
# True  | False |  False  |  True  | False | True 
# False | True  |  False  |  True  | True  | False
# False | False |  False  |  False | True  | True 
#
# --------------------------------------------------------
# CHEAT SHEET:
# AND : Only True if BOTH sides are True.
# OR  : True if AT LEAST ONE side is True.
# NOT : Flips the value (True becomes False, and vice versa).
# ========================================================

# practical

x = True
y = False

#AND operator example ( both value should be true result: True otherwise False)

print( x and y )


# or opereatos example (either one of them must be true to be True otherwise False)
print(x or y )
""" this is test lets see"""


# not operatoes exampl
print(not x)
print(not y)
