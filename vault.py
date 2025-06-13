from auth import verify_master
from encryption import encrypt_password, decrypt_password, generate_key
from data_handler import load_data, save_data
from getpass import getpass
import os

# Generate key once if it doesn't exist
if not os.path.exists("key.key"):
    generate_key()

def add_password():
    account = input("Enter account name: ")
    pwd = getpass("Enter password: ")
    data = load_data()
    data[account] = encrypt_password(pwd)
    save_data(data)
    print(f"Password for {account} added.")

def get_password():
    account = input("Enter account name: ")
    data = load_data()
    if account in data:
        print(f"Password: {decrypt_password(data[account])}")
    else:
        print("Account not found.")

if __name__ == "__main__":
    verify_master()
    while True:
        print("\n--- Password Vault ---")
        print("1. Add new password")
        print("2. Get existing password")
        print("3. Exit")
        choice = input("Choose an option: ")
        
        if choice == '1':
            add_password()
        elif choice == '2':
            get_password()
        elif choice == '3':
            break
        else:
            print("Invalid option.")
