def call():
        from twilio.rest import Client

        account_sid = ''
        auth_token = ''

        client = Client(account_sid, auth_token)

        call = client.calls.create(
            twiml='<Response><Say>Hello from your Twilio !</Say></Response>',
            to='',  # Replace with your recipient's phone number
            from_=''  # Replace with your Twilio phone number
        )

        print(call.sid)  # Print SID to confirm call initiation

def msg():
        from twilio.rest import Client

        account_sid = ''
        auth_token = ''
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            body="Hello from Pyth",
            from_='',  # Your Twilio phone number
            to=''     # The recipient's phone number
        )

        print(f"Message sent with SID: {message.sid}")
