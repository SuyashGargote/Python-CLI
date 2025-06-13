from getpass import getpass

def verify_master():
    MASTER_PASSWORD = "suyash123"  # You can hash & store this later
    entered = getpass("Enter master password: ")
    if entered != MASTER_PASSWORD:
        print("Access denied. Wrong password.")
        exit()
