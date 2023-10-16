# ==================================
#       Introduction
# ==================================

"""
Allllrrrriiiggghhhtttt, this is pwd generator thingy. Take what you want, but just not my pwd (gl btw if you're
trying to steal it lol)
"""

# ================================
#       Dependencies
# ================================

import os
import secrets
import smtplib
import string
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import pyperclip as pc

# ================================
#       Global Variables
# ================================

global pwd_final
date = time.asctime()  # The date variable for options below

# ================================
#       Functions
# ================================

def pwd_criteria_display():  # Communicates to users what current criteria/allowable characters are
    print("\nCurrent Password Criteria: ")  # Display Current Pwd Settings
    crit = []  # List designation variable for simpler communication of criteria

    if string.ascii_letters in chr_vault_1:  # Criteria presentation improvement instruction
        crit.append("Letters")
    if string.digits in chr_vault_1:
        crit.append("Numbers")
    if string.punctuation in chr_vault_1:
        crit.append("Special Characters")

    print(f"{crit}")  # Criteria display expression

def pwd_generation():  # Generates password for users when executed
    while True:
        chr_vault_3 = "".join(map(str, chr_vault_2))  # List conversion to continuous string for secrets lib module gen

        chr_count = int(input("\nEnter the Number of Characters for the New Password: "))  # Chr Amount Selection
        pwd = "".join(secrets.choice(chr_vault_3) for i in range(chr_count))  # Pwd Generator

        global pwd_final
        pwd_final = pwd

        if chr_count <= 100:
            print(f"Password Generated: {pwd}")
            pc.copy(pwd)  # Copy to Clipboard
            print("\n***!Password Copied to Your Clipboard!***")
            print("\n===================================")
            break
        elif chr_count > 100:  # Character limit determinant
            print("***!Character amount too large. Enter a value less than or equal to 100!***")
            continue

def chr_vault_adjustment():  # Allows users to customize allowable characters for generation

    # ***Need to make a multiple choice selection (more than one) for alteration if needed from user***

    print("\nWhat Would You Like to Alter?")
    choice = input("\nEnter 'L' to NOT include Letters in Password"
                   "\nEnter 'N' to NOT include Numbers in Password"
                   "\nEnter 'S' to NOT include Special Characters in Password"
                   "\n\nPlease Enter an Option: ").lower()
    print("\n===================================")

    if choice == 'l':
        chr_vault_2 = chr_vault_1.remove(string.ascii_letters)
        print("Letters Removed from the Next Generated Password.")
    elif choice == 'n':
        chr_vault_2 = chr_vault_1.remove(string.digits)
        print("Numbers Removed from the Next Generated Password.")
    elif choice == 's':
        chr_vault_2 = chr_vault_1.remove(string.punctuation)
        print("Special Characters Removed from the Next Generated Password.")
    print("===================================")

def final_options():  # Options for users after the main program has executed/concluded.
    final_choice = input("\nEnter 'S' to Share"
                         "\nEnter 'E' to Exit"
                         "\nEnter 'R' to Restart"
                         "\n\nPlease Enter an Option: ").lower()
    print("\n===================================")

    if final_choice == "s":
        print("\nEnter 'E' for Email"
              "\nEnter 'T' for Export to Text file")

        sharing_option = input("\nPlease Enter an Option: ").lower()  # Sharing Option Selection
        print("\n===================================")

        if sharing_option == "e":  # Email Sharing Option
            def share_via_email(pwd, recipient_email):
                while True:
                    # Email configuration
                    sender_email = input("Enter Sender's Email Address: ")
                    sender_password = input("Enter Sender's Email Password: ")
                    subject = f"Password Generated on {date}"

                    # Create the email content
                    message = MIMEMultipart()
                    message["From"] = sender_email
                    message["To"] = recipient_email
                    message["Subject"] = subject
                    message.attach(MIMEText(pwd, "plain"))

                    # Connect to the email server and send the message
                    with smtplib.SMTP("smtp.gmail.com", 587) as server:
                        server.starttls()
                        server.login(sender_email, sender_password)
                        server.sendmail(sender_email, recipient_email, message.as_string())

                        print("\n===================================")
                        print(f"\nPassword Successfully Sent to '{recipient_email}'")
                        break

            # Usage:
            recipient_email = input("\nEnter Recipient Email Address: ")
            share_via_email(pwd_final, recipient_email)

        elif sharing_option == "t":  # TXT File Export Option
            filename = f"Pwd_{date}.txt"

            def export_text_file(pwd_final, filename):
                desktop_path = os.path.expanduser("~/Desktop")
                export_path = os.path.join(desktop_path, filename)

                with open(export_path, "w") as file:
                    file.write(pwd_final)
            # Usage:
            export_text_file(pwd_final, filename)
            print("\n***!Text File Saved to Desktop!***")
            print("\n===================================")

    if final_choice == "e":
        quit()
    if final_choice == "r":
        chr_vault_2 = chr_vault_1  # Character Limit Variable Reset and a 'nothing' cmd to avoid syntax error

# ================================
#       Main Program Loop
# ================================

print("\n===================================")  # Intro Tagline
print("\n      'Welcome to Enigmaris'")
print("\n===================================")

while True:
    chr_vault_1 = [string.ascii_letters, string.digits, string.punctuation]  # Initially allowed characters(chr) for gen
    chr_vault_2 = chr_vault_1  # Used for chr_vault_adjustment() function to create an altered collection of chr (i.a.)

    pwd_criteria_display()  # Pwd Criteria Display Function

    print("\nEnter 'C' to Customize the Password Criteria"  # Initial Selection Menu
          "\nEnter 'P' to Generate Password"
          "\nEnter 'E' to Exit")
    initial_choice = input("\nPlease Enter an Option: ").lower()
    print("\n===================================")

    if initial_choice == 'c':  # Character Customization Function
        chr_vault_adjustment()
        pwd_generation()
    elif initial_choice == 'p':  # Pwd Generation Function
        pwd_generation()
    elif initial_choice == 'e':
        exit()

    final_options()  # Final Options Function

# ================================
