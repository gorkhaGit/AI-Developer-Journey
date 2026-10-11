import smtplib
from email.mime.text import MIMEText
sender = "santoshnepali7698@gmail.com"
password = "zusk upms uuci fzyw"

reciever = input("enter reciever email: ")
name = input("enter yout name : ")
msg = MIMEText(f"happy birthday, {name} and have a great day 😛")
msg["Subjet"] = "happy birhtday"
msg["from"] = sender
msg["To"] = reciever
server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.login(sender, password)
server.send_message(msg)
server.quit()
print("Done")