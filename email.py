### --- OOP Email Simulator --- ###

# --- Email Class --- #
class Email:
    # Class variable with default values for emails
    total_emails_created = 0  # Declare the class variable, with a default value, for emails.
    has_been_read_default = False
    is_spam_default = False

    def __init__(self, email_address, subject_line, email_content):
        # Initialise the instance variables for emails.
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content
        self.has_been_read = Email.has_been_read_default
        self.is_spam = Email.is_spam_default  # New attribute to indicate whether the email is marked as spam.

        # Increment the class variable
        Email.total_emails_created += 1  # Increment the total number of emails created.

    def mark_as_read(self):
        # Create the method to change 'has_been_read' emails from False to True.
        self.has_been_read = True  # Change 'has_been_read' to True when the email is marked as read.

    def mark_as_spam(self):
        # Create the method to mark an email as spam.
        self.is_spam = True  # Mark the email as spam.

    def delete_email(self, inbox, deleted_emails):
        # Create the method to delete an email from the inbox.
        inbox.remove(self)
        deleted_emails.append(self)

    @classmethod
    def mark_all_as_read(cls, emails):
        # Class method to mark all emails as read
        for email in emails:
            email.mark_as_read()

# --- Lists --- #
# Initialise an empty list to store the email objects.
inbox = []

# New list to store deleted emails
deleted_emails = []

# --- Functions --- #
def populate_inbox():
    # Create 3 sample emails and add them to the Inbox list.
    email1 = Email("customersupport@asos.com", "Refund", "You will receive your refund in 3-5 working days.")
    email2 = Email("renewal@insurance.com", "Renew Insurance", "Your car's insurance will expire soon. Please renew.")
    email3 = Email("jacob@gmail.com", "Tickets", "I've attached our flight tickets to Kenya.")

    # Add emails to the inbox
    inbox.extend([email1, email2, email3])

def list_emails():
    # Create a function which prints the email’s subject, along with a corresponding number.
    for i, email in enumerate(inbox):
        status = '(Unread)' if not email.has_been_read else ''
        spam_status = '(Spam)' if email.is_spam else ''
        print(f"{i}. {email.subject_line} {status} {spam_status}")

def list_deleted_emails():
    # Create a function to display deleted emails with sender and title
    for i, email in enumerate(deleted_emails):
        print(f"{i}. From: {email.email_address}, Subject: {email.subject_line}")

def read_email(index):
    # Create a function that displays a selected email and sets its 'has_been_read' variable to True.
    if 0 <= index < len(inbox):
        email = inbox[index]
        print(f"\nSubject: {email.subject_line}")
        print(f"From: {email.email_address}")
        print(f"Message: {email.email_content}")

        # Mark the email as read
        email.mark_as_read()
        print(f"\nEmail from {email.email_address} marked as read.\n")

        # Ask the user if they want to mark the email as spam or delete it
        action = input("Do you want to:\n1. Mark as Spam\n2. Delete Email\nEnter the number of your choice (or press Enter to continue): ")

        if action == "1":
            # Mark the email as spam
            email.mark_as_spam()
            print(f"\nEmail from {email.email_address} marked as spam.\n")

        elif action == "2":
            # Delete the email
            email.delete_email(inbox, deleted_emails)
            print(f"\nEmail from {email.email_address} deleted.\n")

        else:
            print("Continuing without marking as spam or deleting.")

    else:
        print("Oops - incorrect input.")

# --- Email Program --- #
# Call the function to populate the Inbox for further use in your program.
populate_inbox()

# Fill in the logic for the various menu operations.
while True:
    user_choice = int(input('''\nWould you like to:
    1. Read an email
    2. View unread emails
    3. View deleted emails
    4. Quit application

    Enter selection: '''))

    if user_choice == 1:
        # Logic to read an email
        list_emails()
        email_index = int(input("Enter the number of the email you want to read: "))
        read_email(email_index)

    elif user_choice == 2:
        # Logic to view unread emails
        unread_emails = [email.subject_line for email in inbox if not email.has_been_read]
        if unread_emails:
            print("\nUnread Email Subjects:")
            for subject in unread_emails:
                print(subject)
        else:
            print("\nNo unread emails.")

    elif user_choice == 3:
        # Logic to view deleted emails
        if deleted_emails:
            print("\nDeleted Email Subjects:")
            list_deleted_emails()
        else:
            print("\nNo deleted emails.")

    elif user_choice == 4:
        # Logic to quit application
        print("Quitting application.")
        break

    else:
        print("Oops - incorrect input.")
