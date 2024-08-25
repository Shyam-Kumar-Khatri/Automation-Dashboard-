def whatsapp():
        import pywhatkit
        monumb = input("tell us mobile number of receiver:\n")
        msg = input("write your msg:\n")
        time_h = input("at what hour you want to send msg:")
        time_m = input("at what minute you want to send msg:") 
        pywhatkit.sendwhatmsg(monumb, msg, int(time_h), int(time_m))

def email():
        import smtplib
        from email.mime.text import MIMEText
        from email.mime.multipart import MIMEMultipart

        # Email account credentials
        sender_email = "toonguru14.coding.try@gmail.com"
        sender_password = ""

        # Email details
        recipient_email = "toonguru14@gmail.com"
        subject = "Hello from my side"
        body = "This is a test email sent from Python."

        # Create the email message
        message = MIMEMultipart()
        message["toonguru14.coding.try@gmail.com"] = sender_email
        message["toonguru14@gmail.com"] = recipient_email
        message["subject"] = subject
        message.attach(MIMEText(body, "plain"))

        # Connect to Gmail's SMTP server
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()  # Secure the connection
            server.login(sender_email, sender_password)
            text = message.as_string()
            server.sendmail(sender_email, recipient_email, text)

        return("Email sent successfully!")

def email_schedule():
        import smtplib
        import schedule
        import time
        from email.mime.multipart import MIMEMultipart
        from email.mime.text import MIMEText

        # Email credentials
        sender_email = "toonguru14.coding.try@gmail.com"
        receiver_email = "toonguru14@gmail.com"
        password = ""

        # Email content
        subject = "Scheduled Email"
        body = "This is a test email sent at a specific time."

        def send_email():
            try:
                # Set up the MIME
                message = MIMEMultipart()
                message['shreyaagrawal0015@gmail.com'] = sender_email
                message['agrawalshreya1003@gmail.com'] = receiver_email
                message['hello'] = subject
                message.attach(MIMEText(body, 'plain'))

                # Connect to the server
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(sender_email, password)

                # Send the email
                server.sendmail(sender_email, receiver_email, message.as_string())
                server.close()

                print("Email sent successfully!")
            except Exception as e:
                print(f"Failed to send email: {e}")

        # Schedule the email to be sent at a specific time
        schedule_time = "2024-07-05 10:43"  # Use the desired time (format: 'YYYY-MM-DD HH:MM')
        schedule_time_struct = time.strptime(schedule_time, "%Y-%m-%d %H:%M")
        schedule_time_seconds = time.mktime(schedule_time_struct)

        # Schedule the email
        schedule.every().day.at(time.strftime("%H:%M", schedule_time_struct)).do(send_email)

        print(f"Email scheduled to be sent at {schedule_time}")

        # Keep the script running to execute the scheduled task
        while True:
            schedule.run_pending()
            time.sleep(1)

def insta():
        from instagrapi import Client

        # Your Instagram credentials
        username = "jskpsx"
        password = ""

        # Initialize the client
        client = Client()
        client.login(username, password)

        # Path to the image you want to upload
        image_path = r'/root/Downloads/levi.jpg'

        # Caption for your post
        caption = "This is a test post from Python"

        # Upload the photo
        client.photo_upload(image_path, caption)

def whatsapp_multi_msg():
        # array data
        import numpy as np
        import pywhatkit as kit
        import time

        # Data array
        data = np.array([
            ('karan', 'ahmedabad', 'nirma', '+919106657225', 'private'),
            ('riyanshi', 'hathras', 'purnima', '+918791949154', '-'),
            ('shreya', 'ahmedabad', 'nirma', '+917802936041', '-'),
            ('shyam', 'shamli', 'KNIT', '+918077681353', '-'),
            ('prem', 'bikaner', 'poornima', '+919766964128', '-'),
        ])

        # Extract WhatsApp numbers
        whatsapp_numbers = data[:, 3]

        # Message to be sent
        message = "Just Ignore This MSG"

        # Function to send messages
        def send_whatsapp_message(number, message):
            try:
                # Send a message to the specified number
                kit.sendwhatmsg_instantly(number, message)
                print(f"Message sent to {number}")
            except Exception as e:
                print(f"Failed to send message to {number}: {e}")

        # Loop through each number and send the message
        for number in whatsapp_numbers:
            send_whatsapp_message(number, message)
            # Wait for 10 seconds to avoid triggering WhatsApp's rate limits
            time.sleep(5)

def purpose():
        import numpy as np

        # Data array
        data = np.array([
            ('karan', 'ahmedabad', 'nirma', '+919106657225', 'private'),
            ('riyanshi', 'hathras', 'purnima', '+918791949154', '-'),
            ('shreya', 'ahmedabad', 'nirma', '+917802936041', '-'),
            ('shyam', 'shamli', 'KNIT', '+918077681353', '-'),
            ('prem', 'bikaner', 'poornima', '+919766964128', '-'),
        ])

        # Function to search by college name and retrieve life purposes
        def get_life_purpose_by_college(college_name):
            # Filter rows where college name matches
            filtered_data = data[data[:, 2] == college_name]

            # Extract life purposes from filtered data
            life_purposes = filtered_data[:, 4]

            # Return life purposes
            return life_purposes

        # Example usage: Search for life purposes of students from "nirma" college
        college_name = input('enter college name:')
        life_purposes = get_life_purpose_by_college(college_name)

        # Print results
        print(f"Life purposes of students from '{college_name}' college:")
        for purpose in life_purposes:
            print(purpose)

def msg_to_not_in_city():
        import numpy as np
        from twilio.rest import Client
        from twilio.base.exceptions import TwilioRestException

        # Your Twilio account SID and auth token
        account_sid = ''
        auth_token = ''
        twilio_phone_number = ''

        # Initialize Twilio client
        client = Client(account_sid, auth_token)

        # Data array
        data = np.array([
            ('karan', 'ahmedabad', 'nirma', '+919106657225', 'private'),
            ('riyanshi', 'hathras', 'purnima', '+918791949154', '-'),
            ('shreya', 'ahmedabad', 'nirma', '+917802936041', '-'),
            ('shyam', 'shamli', 'KNIT', '+918077681353', '-'),
            ('prem', 'bikaner', 'poornima', '+919766964128', '-'),
        ])

        # Message to be sent
        message_text = "Welcome to Pink City, Jaipur"

        # Function to send SMS
        def send_sms(to_number, message):
            try:
                client.messages.create(
                    body=message,
                    from_=twilio_phone_number,
                    to=to_number
                )
                print(f"Message sent to {to_number}")
            except TwilioRestException as e:
                print(f"Failed to send message to {to_number}: {e}")

        # Loop through each person in the data and send SMS if they are not from Jaipur
        for person in data:
            name, city, college, whatsapp_number, life_purpose = person
            if city.lower() != 'jaipur':
                send_sms(whatsapp_number, message_text)
