# List - normal list
# Dictionaries parameters
# Tuples - fixed values
# sets - bag of unique values
# my_list = [1, 2, 3, 4, 5]
# # my_list[1:4:2]
# # my_list[0] = 9
# # my_list[0:4]
# # my_list.append(7)
# # print(my_list)
# # my_list.remove(9)
# # print(my_list)
# # my_list[0]= 1
# # print(my_list)

# my_list.insert(0, 9)
# print(my_list)
# Dictionarie

info = { "name" : "gorkha",
        "age" : 25,
        "address": "melbourne",
        "sim": "optus"
    
        }
info["gender"] = "male"
del info["gender"]
print(info)

another_list = dict(math = 95, science = 87, english = 55)
print(another_list[math])