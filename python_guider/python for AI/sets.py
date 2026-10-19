# " no duplicate allowed
#   no particular order"
# # A list of words with duplicates
# collected_words = ["apple", "banana", "apple", "cherry", "banana"]

# filtered_words = set(collected_words)
# print(filtered_words)

# 
# 
# Intersection (&) — The Mutual Friends

# What it does: Finds items that exist in both sets

ai_vocab = {"python", "data", "model"}
user_input = { "python", "ai", "chat"}
comman = ai_vocab & user_input
print(comman) # intesection "&" le common items ko output dincha

# Union (|) — The Master Guest List hat it does: Combines 
# -twosets together, automatically stripping out any duplicate items
union_words = ai_vocab | user_input
print(f"union | operators : {union_words}")

# Difference (-) — The To-Do List Checkoff
#  What it does: Takes the first set and removes anything that also appears in the second set.\

missing = user_input - ai_vocab
print(f"diffrence - operator: {missing}")