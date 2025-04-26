import smtplib
from email.message import EmailMessage
import time


def send_email():
    #This function is used to send an email.
    # Sender email address
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


    # Connect to the SMTP server 
    server = smtplib.SMTP_SSL('smtp.qq.com', 465)
    # Login to the SMTP server
    server.login(from_email_addr, from_email_pass)
    # Send the message
    server.send_message(msg)
    print('Email sent')


# Record the hour of the start time
startTime = time.localtime(time.time()).tm_hour + 8
lastValue = startTime
print("Time to send the FIRST email of the day")

while True:
    # Get the current time
    seconds = time.time()
    result = time.localtime(seconds)
    Current_Value = result.tm_hour + 8
    # Compare the time
    if lastValue == Current_Value:
        print("IGNORE")
    else:
        difference = Current_Value - lastValue
        if difference >= 4:  # Check every 4 hours
            send_email()
            lastValue = Current_Value
        else:
            print("Hour Difference < 4. Do NOT Email")
    time.sleep(600)  # Check the time every 600 seconds, can be adjusted as needed

