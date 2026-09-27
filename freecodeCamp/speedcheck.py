import time # This brings in Python's built-in time tracking tool

print("Firing up the CPU...")

# 1. Start the stopwatch
start_time = time.time()

# 2. The Heavy Lifting
# We multiply a 5-character string 20 million times to make a 100-million character string
massive_string = "Data-" * 20000000 

# Force the computer to scan all 100 million characters to count the 'D's
d_count = massive_string.count("D")

# 3. Stop the stopwatch
end_time = time.time()

# Calculate the difference
execution_time = end_time - start_time

print(f"Task complete! Found {d_count} 'D's.")
print(f"Your machine processed that in: {execution_time} seconds.")