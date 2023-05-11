import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Set up the email message
sender_email = 'sender@example.com'
receiver_email = 'receiver@example.com'
message = MIMEMultipart()
message['From'] = sender_email
message['To'] = receiver_email
message['Subject'] = 'Test Email'

# Add body to email
body = 'This is a test email sent from Python.'
message.attach(MIMEText(body, 'plain'))

# Connect to SMTP server
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()

# Login to SMTP server
username = 'your-email@gmail.com'
password = 'your-password'
server.login(username, password)

# Send email
text = message.as_string()
server.sendmail(sender_email, receiver_email, text)

# Close the SMTP server connection
server.quit()
