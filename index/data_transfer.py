# data_transfer.py
#import gspread
import logging
from django.conf import settings
#from oauth2client.service_account import ServiceAccountCredentials
from .models import Questions  # Replace 'YourModel' with the name of your Django model representing the data you want to transfer

logging.basicConfig(level=logging.INFO)

def get_data_from_sqlite():
    data = Questions.objects.all()  # Fetch all objects from the model
    return data

def prepare_data_for_sheets(data):
    prepared_data = []
    for item in data:
        row = [item.question, item.question_type , item.required]  # Replace 'field1', 'field2', etc. with your actual field names
        prepared_data.append(row)
    return prepared_data