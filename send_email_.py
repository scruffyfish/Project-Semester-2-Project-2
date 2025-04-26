import smtplib
from email.message import EmailMessage

# Set the sender email and password and recipient email
from_email_addr = "1954295092@qq.com"
from_email_pass = "nskbmuehvrfvbdff"
to_email_addr = "bangumiema@outlook.com"

# Create a message object
msg = EmailMessage()

# Set the email body
msg.set_content("Need Water!")

# Set sender and recipient
msg['From'] = from_email_addr
msg['To'] = to_email_addr

# Set email subject
msg['Subject'] = 'RASPBERRY PI EMAIL'

# Connecting to server and sending email
with smtplib.SMTP_SSL('smtp.qq.com', 465) as server:
    # Login to the SMTP server
    server.login(from_email_addr, from_email_pass)
    # Send the message
    server.send_message(msg)
    print('Email sent successfully')
    server.quit()

