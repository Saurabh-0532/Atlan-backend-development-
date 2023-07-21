# utils.py (you can place this in any app)

from twilio.rest import Client
from django.conf import settings
from django.shortcuts import render


def send_sms(to_phone_number, message):
    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
    
    try:
        message = client.messages.create(
            body=message,
            from_=settings.TWILIO_PHONE_NUMBER,
            to=to_phone_number
        )
        return message.sid
    except Exception as e:
        # Handle any errors that might occur during sending the SMS
        print(f"Failed to send SMS: {e}")
        return None
        


def send_sms_view(request):
    # Some logic to get the recipient's phone number and message
    to_phone_number = '+919517097736'  # Replace with the recipient's phone number
    message = 'Hello Prabhakar, it me saurabh'
    print('in twilio func')
    
    # Send the SMS
    '''if send_sms(to_phone_number, message):
        return render(request, 'success.html')
    else:
        return render(request, 'error.html')'''

