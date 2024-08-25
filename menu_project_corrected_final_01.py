print("\t\tWelcome, tell us what action you want to perform")
print("\t\t------------------------------------------------")
print("\n\n")

ch = None

while ch != "exit":
    ch = input(":-")




    if "menu" in ch.lower():
        print("""following commands are available to execute:-
        NOTE:- "+" indicates that those all words should be included in the command.
               "/" indicates that you can use any of the commands written there to perform the given operation.
         0. menu :-
                show all the commands available in menu project

         1. whatsapp + send :-
                send whatsapp msg to a single person or group of people

         2. not live in jaipur / not from jaipur :-
                send whatsapp msg to those who don't live in jaipur

         3. sms / msg :-
                send sms to someone

         4. email :-
                send email to someone

         5. search / google :-
                search over google and show top 6 results as output

         6. call / phone / phone call :-
                give a phone call to someone

         7. insta :-
                to post over your instagram account

         8. purpose :-
                show the purpose section from collected data

         9. video by ipwebcam / ipwebcam / video :-
                to start a video capture from your mobile camera

        10. remote login / ssh :-
                to remote login in any OS by SSH protocol

        11. rainbow + text :-
                to convert any text in RAINBOW colors

        12. change firefox name and icon :-
                to change firefox name and logo
 
        13. launch firefox :- 
                launch firefox

        14. linear regression :-
                linear regression

        15. launch EC2 :-
                launch EC2 instances

        16. insert data in mongoDb database :-
                insert data in mongoDb database

        17. email with attached image :-
                email with attached image

        18. gemini text-to-text :-
                Gemini text-to-text

        19. click photo of whoever sit infront of the system or laptop :-
                click photo of whoever sit infront of the system or laptop

        20. exit :-
                to exit the program""")

    elif "send" in ch.lower() and "whatsapp" in ch.lower():
        group_msg = input("Do you want to send msg to group [y/n]:")
        if group_msg == "n":
            from module_social_media import whatsapp
            whatsapp()
        else:
            from module_social_media import whatsapp_multi_msg
            whatsapp_multi_msg()

    elif "call" in ch.lower() or "phone call" in ch.lower() or "phone" in ch.lower():
        from module_sim import call
        call()

    elif "sms" in ch.lower() or "msg" in ch.lower():
        from module_sim import msg
        msg()

    elif "email" in ch.lower():
        choice = input("do you want to schedule it for a specific time [y/n]:")
        if choice == "n":
            from module_social_media import email
            email()
        elif choice == "y":
            from module_social_media import email_schedule
            email_schedule()

    elif "search" in ch.lower() or "google" in ch.lower():
        from module_internet import google_search
        google_search()

    elif "insta" in ch.lower():
        from module_social_media import insta
        insta()

    elif "send" in ch.lower() and (("whatsapp" in ch.lower() and "group" in ch.lower()) or ("whatsapp" in ch.lower() and "bulk" in ch.lower())):
        from module_social_media import whatsapp_multi_msg
        whatsapp_multi_msg()

    elif "purpose" in ch.lower():
        from module_social_media import purpose
        purpose()

    elif "not live in jaipur" in ch.lower() or "not from jaipur" in ch.lower():
        from module_social_media import msg_to_not_in_city
        msg_to_not_in_city()

    elif "video by ipwebcam" in ch.lower() or "video" in ch.lower() or "ipwebcam" in ch.lower():
        from module_os import video_ipwebcam
        video_ipwebcam()

    elif ("remote login" in ch.lower() or "ssh" in ch.lower()) and not("send" in ch.lower() or "transfer" in ch.lower()):
        hostname = input("enter hostname or IP:")
        port = input("enter port number [default port 22]:")
        username = input("enter username:")
        password = input("enter password:") 
        command = input("enter command you want to run:")

        from module_remote_os import ssh_login
        ssh_login(hostname, port, username, password, command)

    elif "rainbow" in ch.lower() and "text" in ch.lower():
        text = input("enter the text:")
        from module_os import rainbow_text
        rainbow_text(text)

    elif "change firefox name and icon" in ch.lower():
        import os

        # Define the file path
        file_path = "/usr/share/applications/firefox.desktop"

        # Ensure the script is running as root
        if os.geteuid() != 0:
            raise PermissionError("This script must be run as root.")

        # Read the content of the file
        with open(file_path, "r") as file:
            lines = file.readlines()

        # Modify the lines
        with open(file_path, "w") as file:
            for line in lines:
                if line.startswith("Name="):
                    file.write("Name=Google\n")
                elif line.startswith("Icon="):
                    file.write("Icon=/root/Downloads/levi.jpg\n")
                else:
                    file.write(line)

        print("Changes have been made successfully.")
 
    elif "launch firefox" in ch.lower():
        import subprocess
        url="https://www.google.com"
        subprocess.Popen(["firefox",url])

    elif "linear regression" in ch.lower():
        import pandas 
        db=pandas.read_csv("Markx.txt")
        y=db["marks"]
        x=db["hours"]
        x=x.values.reshape(-1,1)
        from sklearn.linear_model import LinearRegression
        #model create 
        model=LinearRegression()
        #model train
        model.fit(x,y)
        model.predict([[8]])

    elif "launch EC2" in ch.lower():
        import boto3
        from flask import Flask

        app=Flask(_name_)

        myec2=boto3.resource(
            service_name="ec2",
            region_name="ap-south-1",
            aws_access_key_id="",
            aws_secret_access_key=""
        )
        @app.route("/launch")
        def oslaunch():
            myec2.create_instances(
                InstanceType="t2.micro",
                ImageId="ami-0ec0e125bb6c6e8ec",
                MaxCount=1,
                MinCount=1
            )
            return "ok"
        app.run()

    elif "insert data in mongoDb database" in ch.lower():
        import pymongo
        connection=pymongo.MongoClient("mongodb://localhost:27017/") #connection stablished
        dbname=connection["komal"]
        nnn=dbname["haq"]
        nnn.insert_many([{"name":"jack"},{"name":"rock"},{"phone":"6789"}])
        for data in nnn.find():
            print(data)

    elif "email with attached image" in ch.lower():
        def sendingEmailWithAttach(Sender_Email):
            import smtplib
            from email.mime.text import MIMEText 
            from email.mime.application import MIMEApplication
            from email.mime.multipart import MIMEMultipart

            server=smtplib.SMTP("smtp.gmail.com",587)
            server.starttls()

            msg=MIMEMultipart()
            msg['From']=sender_Emial  #Enter sender Email
            msg['To']=reicer_email      #Enter receiver email
            msg['Subject']="Welcome to Linux World"
            msg.attach(MIMEMultipart('Summer Internship is started from 1 july'))
            with open('typeSpeed.png','rb') as f:
                attachment=MIMEApplication(f.read())
                media_file='typeSpeed.png'
                attachment.add_header('Content-Disposition','attachment',filename=media_file)
                msg.attach(attachment)
            server.login('sender_email','pvesndeundxwrukl')   #replace Accordingly
            server.sendmail('senderEmail','receiverMail',msg.as_string())   #replace Accordingly
            server.quit()
            print("-------------Email Sent with Attachment------------")

    elif "gemini text-to-text" in ch.lower():
        import os
        import google.generativeai as gemai
        gemai.configure(api_key='AIzaSyBFTaMYHIA8IVg65uVJjHaDiy7vsXS4qqU')
        model=gemai.GenerativeModel(model_name='gemini-1.5-flash')
        response=model.generate_content('About Earth in 2 line')
        print(response.text)

    elif "click photo of whoever sit infront of the system or laptop" in ch.lower():
        import cv2
        import mediapipe as mp
        import time

        # Initialize the webcam
        cap = cv2.VideoCapture(0)

        # Initialize the MediaPipe Face Detection
        mp_face_detection = mp.solutions.face_detection
        mp_drawing = mp.solutions.drawing_utils

        face_detection = mp_face_detection.FaceDetection(min_detection_confidence=0.5)

        # Initialize a counter and a flag
        photo_counter = 0
        face_detected = False

        # Flag to control the visibility of the window
        show_window = False

        # Function to save the captured image
        def save_photo(frame, counter):
            filename = f'photo_{counter}.jpg'
            cv2.imwrite(filename, frame)
            print(f"Photo saved as {filename}")

        # Mouse callback function to show the window
        def on_mouse(event, x, y, flags, param):
            global show_window
            if event == cv2.EVENT_LBUTTONDOWN:
                show_window = not show_window

        # Create a named window and set the mouse callback
        cv2.namedWindow("Webcam", cv2.WINDOW_NORMAL)
        cv2.setMouseCallback("Webcam", on_mouse)

        # Main loop
        while True:
            success, frame = cap.read()
            if not success:
                break

            # Convert the frame to RGB
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Perform face detection
            results = face_detection.process(rgb_frame)

            # Check if a face is detected
            if results.detections:
                if not face_detected:
                    face_detected = True
                    photo_counter += 1
                    save_photo(frame, photo_counter)

                # Draw face detections
                for detection in results.detections:
                    mp_drawing.draw_detection(frame, detection)
            else:
                face_detected = False

            # Display the frame if the window is supposed to be shown
            if show_window:
                cv2.imshow("Webcam", frame)

            # Check if 'q' is pressed to break the loop
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # Release the webcam and close the window
        cap.release()
        cv2.destroyAllWindows()


    elif (("remote login" in ch.lower() or "ssh" in ch.lower()) and ("transfer" in ch.lower() or "send" in ch.lower())):
        hostname = input("enter hostname or IP:")
        port = input("enter port number [default port 22]:")
        username = input("enter username:")
        password = input("enter password:")

        send_file_to_remote(hostname, port, username, password)


    elif "exit" in ch.lower():
        break

    else:
        print("""don't know this command, following commands are available to execute:-
        NOTE:- "+" indicates that those all words should be included in the command.
               "/" indicates that you can use any of the commands written there to perform the given operation.
         0. menu :-
                show all the commands available in menu project

         1. whatsapp + send :-
                send whatsapp msg to a single person or group of people

         2. not live in jaipur / not from jaipur :-
                send whatsapp msg to those who don't live in jaipur

         3. sms / msg :-
                send sms to someone

         4. email :-
                send email to someone

         5. search / google :-
                search over google and show top 6 results as output

         6. call / phone / phone call :-
                give a phone call to someone

         7. insta :-
                to post over your instagram account

         8. purpose :-
                show the purpose section from collected data

         9. video by ipwebcam / ipwebcam / video :-
                to start a video capture from your mobile camera

        10. remote login / ssh :-
                to remote login in any OS by SSH protocol

        11. rainbow + text :-
                to convert any text in RAINBOW colors

        12. change firefox name and icon :-
                to change firefox name and logo
 
        13. launch firefox :- 
                launch firefox

        14. linear regression :-
                linear regression

        15. launch EC2 :-
                launch EC2 instances

        16. insert data in mongoDb database :-
                insert data in mongoDb database

        17. email with attached image :-
                email with attached image

        18. gemini text-to-text :-
                Gemini text-to-text

        19. click photo of whoever sit infront of the system or laptop :-
                click photo of whoever sit infront of the system or laptop

        20. exit :-
                to exit the program""")
