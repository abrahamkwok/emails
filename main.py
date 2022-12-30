from keep_alive import keep_alive
import os
import smtplib
import imghdr
from email.message import EmailMessage
import time

#chores
def messages(input):
  if input == 0:
    return "Josh: Trash, Enoch: Bathroom, Adit: Floor, Abraham: Dishes"
  elif input == 1:
    return "Josh: Dishes, Enoch: Trash, Adit: Bathroom, Abraham: Floor"
  elif input == 2:
    return "Josh: Floor, Enoch: Dishes, Adit: Trash, Abraham: Bathroom"
  else:
    return "Josh: Bathroom, Enoch: Floor, Adit: Dishes, Abraham: Trash"

#images/pdfs for other stuff
    #with open('spiderman.jpg', 'rb') as f:
    #  file_data = f.read()
    #  file_type = imghdr.what(f.name)
    #  file_name = f.name

    #msg.add_attachment(file_data, maintype = 'image', subtype = 'file_type', filename = file_name)


#email sending
def send_mail(input):
  EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
  EMAIL_PASSWORD = os.getenv("EMAIL_PASS")
  contacts = ["abrahamkwok628@gmail.com", "joshschang@berkeley.edu", "estseng@berkeley.edu", "aditgupta@berkeley.edu"]
  msg = EmailMessage()
  msg['Subject'] = 'chores'
  msg['From'] = 'EMAIL_ADDRESS'
  msg['To'] = ", ".join(contacts)
  msg.set_content(messages(input))
  with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)

keep_alive()
input = 0

while True:
  send_mail(input % 4)
  input += 1
  
  time.sleep(604800)