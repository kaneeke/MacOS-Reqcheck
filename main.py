import platform
import psutil
import time
from colorama import init, Fore

# Initialize colorama
init()

def check_system_requirements():
    print("\nStarting system requirements check...")
    time.sleep(1)

    print("Checking processor architecture...")
    time.sleep(1)
    architecture = platform.architecture()[0]
    if '64' not in architecture:
        return False, "System does not have a 64-bit processor"
        
    print("Checking available disk space...")
    time.sleep(1)
    disk_usage = psutil.disk_usage('/')
    if disk_usage.free < 10 * 1024 * 1024 * 1024:  # 10GB in bytes
        return False, "Insufficient free space on the hard drive"

    print("Checking available memory (RAM)...")
    time.sleep(1)
    memory = psutil.virtual_memory().total
    if memory < 8 * 1024 * 1024 * 1024: 
        return False, "Insufficient memory (RAM)"

    print("System requirements check completed.")
    time.sleep(1)

    return True, "System meets the requirements to run MacOS"

def main_menu():
    rainbow_title = f"""
{Fore.RED} __  __          _____ ____   _____           _               _
{Fore.GREEN}|  \/  |   /\   / ____/ __ \ / ____|         | |             | |
{Fore.YELLOW}| \  / |  /  \ | |   | |  | | (___ ______ ___| |__   ___  ___| | _____ _ __
{Fore.CYAN}| |\/| | / /\ \| |   | |  | |\___ \______/ __| '_ \ / _ \/ __| |/ / _ \ '__|
{Fore.BLUE}| |  | |/ ____ \ |___| |__| |____) |    | (__| | | |  __/ (__|   <  __/ |
{Fore.MAGENTA}|_|  |_/_/    \_\_____\____/|_____/      \___|_| |_|\___|\___|_|\_\___|_|

                                                                              """
    print(rainbow_title)
    print(f"{Fore.WHITE}Main Menu:")
    print(f"{Fore.WHITE}1. Check System Requirements")
    print(f"{Fore.WHITE}2. Exit")

if __name__ == "__main__":
    main_menu()
    choice = input("Enter your choice (1/2): ")

    if choice == '1':
        meets_requirements, message = check_system_requirements()
        print(message)
        if meets_requirements:
            print("Yes, your system can run MacOS.")
        else:
            print("No, your system cannot run MacOS.")
    elif choice == '2':
        print("Exiting the program. Goodbye!")
    else:
        print("Invalid choice. Please enter 1 or 2.")
