### --- OOP Email Simulator --- ###

# --- Email Class --- #
class Email:
    total_emails_created = 0
    has_been_read_default = False
    is_spam_default = False

    def __init__(self, email_address, subject_line, email_content):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content
        self.has_been_read = Email.has_been_read_default
        self.is_spam = Email.is_spam_default

        Email.total_emails_created += 1

    def mark_as_read(self):
        self.has_been_read = True

    def mark_as_spam(self):
        self.is_spam = True

    def delete_email(self, inbox, deleted_emails):
        inbox.remove(self)
        deleted_emails.append(self)

    @classmethod
    def mark_all_as_read(cls, emails):
        for email in emails:
            email.mark_as_read()

# Function to list all emails in the inbox
def list_all_emails(inbox):
    if inbox:
        print("\nAll Email Subjects:")
        for i, email in enumerate(inbox):
            status = '(Unread)' if not email.has_been_read else ''
            spam_status = '(Spam)' if email.is_spam else ''
            print(f"{i}. {email.subject_line} {status} {spam_status}")
    else:
        print("\nNo emails in the inbox.")

# Function to list all spam emails
def list_spam_emails(spam_emails):
    if spam_emails:
        print("\nSpam Email Subjects:")
        for i, email in enumerate(spam_emails):
            print(f"{i}. From: {email.email_address}, Subject: {email.subject_line}")
    else:
        print("\nNo spam emails.")

# Function to list all deleted emails
def list_deleted_emails(deleted_emails):
    for i, email in enumerate(deleted_emails):
        print(f"{i}. From: {email.email_address}, Subject: {email.subject_line}")

# Function to read and perform actions on an email
def read_email(index, inbox, deleted_emails, spam_emails):
    if 0 <= index < len(inbox):
        email = inbox[index]
        if not email.is_spam:  # Check if the email is not marked as spam
            print(f"\nSubject: {email.subject_line}")
            print(f"From: {email.email_address}")
            print(f"Message: {email.email_content}")

            email.mark_as_read()
            print(f"\nEmail from {email.email_address} marked as read.\n")

            action = input("Do you want to:\n1. Mark as Spam\n2. Delete Email\nEnter the number of your choice (or press Enter to continue): ")

            if action == "1":
                email.mark_as_spam()
                print(f"\nEmail from {email.email_address} marked as spam.\n")

                # Move the email to the spam folder
                inbox.remove(email)
                spam_emails.append(email)
                print(f"\nEmail from {email.email_address} moved to spam folder.\n")

            elif action == "2":
                email.delete_email(inbox, deleted_emails)
                print(f"\nEmail from {email.email_address} deleted.\n")

            else:
                print("Continuing without marking as spam or deleting.")

        else:
            print("\nThis email is marked as spam and cannot be read.\n")

    else:
        print("Oops - incorrect input.")

# Function to create sample emails and add them to the inbox
def populate_inbox():
    email1 = Email("customersupport@asos.com", "Refund", "You will receive your refund in 3-5 working days.")
    email2 = Email("renewal@insurance.com", "Renew Insurance", "Your car's insurance will expire soon. Please renew.")
    email3 = Email("jacob@gmail.com", "Tickets", "I've attached our flight tickets to Kenya.")

    inbox.extend([email1, email2, email3])

# Lists
inbox = []
deleted_emails = []
spam_emails = []

# Email Program
populate_inbox()

while True:
    user_choice = input('''\nWould you like to:
    1. Read an email
    2. View unread emails
    3. View spam emails
    4. View deleted emails
    5. Quit application

    Enter selection: ''')

    if user_choice == "1":
        list_all_emails(inbox)
        email_index = int(input("Enter the number of the email you want to read: "))
        read_email(email_index, inbox, deleted_emails, spam_emails)

    elif user_choice == "2":
        unread_emails = [email.subject_line for email in inbox if not email.has_been_read]
        if unread_emails:
            print("\nUnread Email Subjects:")
            for subject in unread_emails:
                print(subject)
        else:
            print("\nNo unread emails.")

    elif user_choice == "3":
        list_spam_emails(spam_emails)

    elif user_choice == "4":
        list_deleted_emails(deleted_emails)

    elif user_choice == "5":
        print("Quitting application.")
        break

    else:
        print("Oops - incorrect input.")

