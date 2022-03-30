import os
import time


def clearConsole():
    # os.system('cls' if os.name == 'nt' else 'clear')
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


# for x in range(10):
#     print("_"*x)
#     time.sleep(0.2)
#     clearConsole()
