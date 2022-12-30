from keep_alive import keep_alive
import os
import smtplib
from email.message import EmailMessage
import requests
import time

#chores
def messages(input):

  #quotes
  quoteOfWeek = "http://api.quotable.io/random"
  random_quote = requests.get(quoteOfWeek).json()
  content = random_quote["content"]
  author = random_quote["author"]
  quote = content + "\n\n" + "By " + author
  
  if input == 0:
    return f"""
    <html>
      <body>
        <p> Josh: Trash, Enoch: Bathroom, Adit: Floor, Abraham: Dishes
        <p> {quote} </p>
      </body>
    </html>
    """        
  elif input == 1:
    return f"""
    <html>
      <body>
        <p> Josh: Dishes, Enoch: Trash, Adit: Bathroom, Abraham: Floor
        <p> {quote} </p>
      </body>
    </html>
    """   
  elif input == 2:
    return f"""
    <html>
      <body>
        <p> Josh: Floor, Enoch: Dishes, Adit: Trash, Abraham: Bathroom
        <p> {quote} </p>
      </body>
    </html>
    """    
  else:
    return f"""
    <html>
      <body>
        <p> Josh: Bathroom, Enoch: Floor, Adit: Dishes, Abraham: Trash
        <p> {quote} </p>
      </body>
    </html>
    """  

#email sending
def send_mail(input):

  #account
  EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
  EMAIL_PASSWORD = os.getenv("EMAIL_PASS")

  #contacts
  email2 = os.getenv("email2")
  email3 = os.getenv("email3")
  email4 = os.getenv("email4")
  
  #setting up email
  contacts = [EMAIL_ADDRESS, email2, email3, email4]
  msg = EmailMessage()
  msg['Subject'] = 'test'
  msg['From'] = 'EMAIL_ADDRESS'
  #msg['To'] = 'abrahamkwok628@gmail.com'
  msg['To'] = ", ".join(contacts)

  #dog pics
  dog_info = requests.get('https://api.thedogapi.com/v1/images/search').json()[0]
  dog_image_url = dog_info['url']

  #sending message
  msg.set_content(messages(input))
  msg.add_alternative(messages(input) + f'<br/><img src="{dog_image_url}" width="300px">', subtype='html')

  with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)

#starting server
keep_alive()
input = 0

#runs function
while True:
  send_mail(input % 4)
  input += 1
  
  time.sleep(604800)
