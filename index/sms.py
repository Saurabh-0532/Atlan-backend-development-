# utils.py (you can place this in any app)

from twilio.rest import Client
from django.conf import settings
from django.shortcuts import render
from .data_transfer import content_for_sms
from .sql_query import return_value_sms


def send_sms(to_phone_number, message):
    print("in sms func")
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
    content = content_for_sms()
    total_message = ''
    phone_no = return_value_sms()
    #print(content)
    x = ' '.join(content)
    total_message = "welcomw to atlan ur detail are : " + x
    to_phone_number = phone_no# Replace with the recipient's phone number
    message = total_message
    
    print(message)
    send_sms(to_phone_number, message)
    # Send the SMS
    '''if send_sms(to_phone_number, message):
        return render(request, 'success.html')
    else:
        return render(request, 'error.html')'''

