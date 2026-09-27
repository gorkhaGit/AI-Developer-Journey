import platform
import os

print("--- Backend Server Hardware Check ---")
print(f"Operating System: {platform.system()} {platform.release()}")
print(f"Processor Architecture: {platform.processor()}")
# cpu_count() shows how many logical cores your machine has for processing tasks
print(f"Available CPU Cores: {os.cpu_count()}")