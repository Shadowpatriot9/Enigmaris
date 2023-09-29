###################################
"""Allllrrrriiiggghhhtttt, this is pwd generator thingy. Take what you want, but just not my pwd (gl btw if you're
trying to steal it lol)"""
###################################
# Dependencies
import pyperclip as pc
import string
import secrets
###################################
# Global Variables
chr_vault_1 = [string.ascii_letters, string.digits, string.punctuation]
###################################
# Functions
def pwd_criteria_display():
    print("\nCurrent Password Criteria: ")  # Display Current Pwd Settings
    print(f"{chr_vault_1}")

def chr_vault_adjustment():
    print("\nWhat Would You Like to Alter?")
    choice = input("\nEnter 'L' to NOT include Letters in Password"
                   "\nEnter 'N' to NOT include Numbers in Password"
                   "\nEnter 'S' to NOT include Special Characters in Password"
                   "\n\nPlease Enter an Option: ").lower()
    print("\n===================================")

    if choice == 'l':
        chr_vault_1.remove(string.ascii_letters)
        print("Letters Removed from the Next Generated Password.")
    elif choice == 'n':
        chr_vault_1.remove(string.digits)
        print("Numbers Removed from the Next Generated Password.")
    elif choice == 's':
        chr_vault_1.remove(string.punctuation)
        print("Special Characters Removed from the Next Generated Password.")
    print("===================================")

def pwd_generation():
    chr_vault_2 = "".join(map(str, chr_vault_1))  # List conversion to continuous string for secrets module gen
    chr_count = int(input("\nEnter the Number of Characters Needed for the New Password: "))  # Chr Amount Selection
    pwd = "".join(secrets.choice(chr_vault_2) for i in range(chr_count))  # Pwd Generator

    print(f"Password Generated: {pwd}")  # Result Print
    pc.copy(pwd)  # Copy to Clipboard
    print("\n***Password Copied to Your Clipboard***")  # Copy Acknowledgement
    print("\n===================================")

def final_options():
    final_choice = input("\nEnter 'S' to Share"
                         "\nEnter 'E' to Exit"
                         "\nEnter 'R' to Restart"
                         "\n\nPlease Enter an Option: ").lower()
    if final_choice == "s":
        print("Shared")
    if final_choice == "e":
        quit()
    if final_choice == "r":
        # ***IP*** chr_vault_2 = chr_vault_1  # Character Limit Variable Reset
        print("blah")  # Need a better continuation method than a print
###################################
# Main Program Loop
print("\n===================================")  # Intro Tagline
print("\n'Welcome to Enigmaris'")

while True:
    print("\n===================================")
    print("\nEnter 'C' for Password Criteria Customization"  # Initial Selection Menu
          "\nEnter 'P' to Generate Password")

    pwd_criteria_display()  # Pwd Criteria Display Function

    initial_choice = input("\nPlease Enter an Option: ").lower()
    print("\n===================================")

    if initial_choice == 'c':  # Character Customization Function
        chr_vault_adjustment()
        pwd_generation()
    elif initial_choice == 'p':  # Pwd Generation Function
        pwd_generation()

    final_options()  # Final Options Function
###################################
