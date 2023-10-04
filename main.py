"""
Allllrrrriiiggghhhtttt, this is pwd generator thingy. Take what you want, but just not my pwd (gl btw if you're
trying to steal it lol)
"""

# ================================
#       Dependencies
# ================================

import pyperclip as pc
import string
import secrets

# ================================
#       Global Variables
# ================================


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

def chr_vault_adjustment():  # Allows users to customize allowable characters for generation
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

def pwd_generation():  # Generates password for users when executed
    while True:
        chr_vault_3 = "".join(map(str, chr_vault_2))  # List conversion to continuous string for secrets lib module gen

        chr_count = int(input("\nEnter the Number of Characters for the New Password: "))  # Chr Amount Selection
        pwd = "".join(secrets.choice(chr_vault_3) for i in range(chr_count))  # Pwd Generator

        if chr_count <= 100:
            print(f"Password Generated: {pwd}")
            pc.copy(pwd)  # Copy to Clipboard
            print("\n***Password Copied to Your Clipboard***")
            print("\n===================================")
            break
        elif chr_count >= 100:  # Character limit determinant
            print("***!Character amount too large. Enter a value less than or equal to 100!***")
            continue

def final_options():  # Options for users after the main program has executed/concluded.
    final_choice = input("\nEnter 'S' to Share"
                         "\nEnter 'E' to Exit"
                         "\nEnter 'R' to Restart"
                         "\n\nPlease Enter an Option: ").lower()
    if final_choice == "s":
        """
        # Options for sharing: email draft, URL or QR code, SMS, export to txt file (or PDF?)
            print("Shared")
            print("Choose a sharing option:")
            print("1. Email")
            print("2. URL or QR code")
            print("3. SMS")
            print("4. Export to text file")
        
            # Get user's choice
            sharing_option = input("Enter the number of your choice: ")
        
            if sharing_option == "1":
                # Code for sharing via email
                print("Share via email")
                
                
                import smtplib
                from email.mime.text import MIMEText
                from email.mime.multipart import MIMEMultipart
                
                def share_via_email(password, recipient_email):
                    # Email configuration
                    sender_email = "your_email@gmail.com"
                    sender_password = "your_password"
                    subject = "Shared Password"
                
                    # Create the email content
                    message = MIMEMultipart()
                    message["From"] = sender_email
                    message["To"] = recipient_email
                    message["Subject"] = subject
                    message.attach(MIMEText(password, "plain"))
                
                    # Connect to the email server and send the message
                    with smtplib.SMTP("smtp.gmail.com", 587) as server:
                        server.starttls()
                        server.login(sender_email, sender_password)
                        server.sendmail(sender_email, recipient_email, message.as_string())
                
                # Usage:
                recipient_email = "recipient@example.com"
                share_via_email("YourGeneratedPassword123", recipient_email)
                
                        
            elif sharing_option == "2":
                # Code for sharing via URL or QR code
                print("Share via URL or QR code")
                     
                        
            elif sharing_option == "3":
                # Code for sharing via SMS
                print("Share via SMS")

                from twilio.rest import Client
                def share_via_sms(password, recipient_phone):
                    account_sid = "your_account_sid"
                    auth_token = "your_auth_token"
                    client = Client(account_sid, auth_token)
                    message = client.messages.create(
                        body=f"Your shared password: {password}",
                        from_="your_twilio_number",
                        to=recipient_phone
                    )
                # Usage:
                recipient_phone = "+1234567890"
                share_via_sms("YourGeneratedPassword123", recipient_phone)


            elif sharing_option == "4":
                # Code for exporting to a text file
                print("Export to text file")
                
                def export_to_text_file(password, filename):
                with open(filename, "w") as file:
                    file.write(password)
                # Usage:
                export_to_text_file("YourGeneratedPassword123", "password.txt")


            else:
                print("Invalid choice. Please select a valid sharing option.")
        """
    if final_choice == "e":
        quit()
    if final_choice == "r":
        chr_vault_2 = chr_vault_1  # Character Limit Variable Reset and a 'nothing' cmd to avoid syntax error

# ================================
#       Main Program Loop
# ================================

print("\n===================================")  # Intro Tagline
print("\n'Welcome to Enigmaris'")

while True:
    chr_vault_1 = [string.ascii_letters, string.digits, string.punctuation]  # Initially allowed characters(chr) for gen
    chr_vault_2 = chr_vault_1  # Used for chr_vault_adjustment() function to create an altered collection of chr (i.a.)

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

# ================================
