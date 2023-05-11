import cv2
from playsound import playsoundimport sendgrid
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


fire_cascade = cv2.CascadeClassifier('fire_train_algo.xml')

cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    fire = fire_cascade.detectMultiScale(frame, 1.2, 5)

    for (x,y,w,h) in fire:
        cv2.rectangle(frame,(x-20,y-20),(x+w+20,y+h+20),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        print("fire is detected")
        playsound('audio.mp3')
        
        # Set up the email message
        sender_email = 'sender@example.com'
        receiver_email = 'receiver@example.com'
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = receiver_email
        message['Subject'] = 'Test Email'

        # Add body to email
        body = 'This is a test email sent for Fire Alert'
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


    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

''' code is written by Aniket Wandile
    https://aniketwandile.netlify.app/'