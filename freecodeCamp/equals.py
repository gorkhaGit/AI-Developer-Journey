import requests # 1. Put the tool on the workbench

# 2. Use the tool to go to a website and get data
response = requests.get("https://api.github.com") 

# 3. Print the result to the screen so you can see it worked
print(response.status_code)
print("hello there")