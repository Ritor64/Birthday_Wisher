import os

# SMTP details
from_addr = "PASTE SENDER EMAIL HERE"
to_addr = "PASTE RECIPIENT EMAIL HERE"
password = "PASTE SENDER EMAIL PASSWORD HERE"
smtp_server = "SMTP SERVER FOR SENDER EMAIL"
# e.g. Google will be 'smtp.google.com
# GMAIL require to lower security settings to send emails via this software

#Path details
ROOT_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__), '..'))

# Folder name where the python script is
main_folder = 'Birthday_Wisher'

# Folder name where the letters are. Should be in the scrypt folder
letters_folder = 'letter_templates'

# Misc
email_subject = 'Happy Birthday'