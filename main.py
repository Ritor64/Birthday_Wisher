import smtplib
import datetime as dt
import random
import csv
from Birthday_Wisher.config.definitions import *

'''Function to send email'''
def send_me_mail(to_addr, from_addr, password, smtp_server, message):
    with smtplib.SMTP(f"{smtp_server}") as connection:
        connection.starttls()
        connection.login(user=from_addr, password=password)
        connection.sendmail(from_addr=from_addr,
                            to_addrs=f"{to_addr}",
                            msg=f"Subject:{email_subject}\n\n{message}"
        )

with open('quotes.txt') as f:
    all_quotes = f.readlines()
    random_quote = random.choice(all_quotes)

# Initializing the titles and rows list
fields = []
rows = []

# Gathering date data
now = dt.datetime.now()
year = now.year
month = now.month
day = now.day

# Preparing random letter file
letters_path = os.path.join(ROOT_DIR, f'{main_folder}', f'{letters_folder}')
random_letter_filename = random.choice(os.listdir(f'{letters_path}'))
letter_filepath = os.path.join(f'{letters_path}', f'{random_letter_filename}')

'''Function to prepare the email text'''
def letter_details(letter_filepath):
    with open(letter_filepath, 'r') as letter:
        message = letter.read()

        # Replace the '[NAME]' with normal name
        message = message.replace('[NAME]', birth_name)
        return message

# Reading csv file
with open('birthdays.csv') as birth_file:
    birth_data = csv.reader(birth_file, delimiter=',')

# Extracting field names and data
    fields = next(birth_data)
    for row in birth_data:
        rows.append(row)
    birth_name = row[0]
    recipient = row[1]
    b_year = int(row[2])
    b_month = int(row[3])
    b_day = int(row[4])
# Sending letter to recipient
    if year == b_year and month == b_month and day == b_day:
        send_me_mail(recipient, from_addr, password, smtp_server, letter_details(letter_filepath))
