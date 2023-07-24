# data_transfer.py
import gspread
import logging
from django.conf import settings
from oauth2client.service_account import ServiceAccountCredentials
from .models import Questions, Answer# Replace 'YourModel' with the name of your Django model representing the data you want to transfer
from .sql_query import answer_to_return_gsheet

logging.basicConfig(level=logging.INFO)

def get_data_from_sqlite():
    data = Questions.objects.all()  #fetching the values from the index_questions table or from questions model
    return data
def get_data_from_answers():        #fetching the values from the index_answer table or from Answer model
    res = Answer.objects.all()
    return res
last_enrty_of_sheet =[0]
def prepare_data_for_sheets(data):
    prepared_data = []
    row = []
    
    for item in data:
        row.append(item.question)  
    prepared_data.append(row)
    res = answer_to_return_gsheet()
    for ans in res:
        prepared_data.append(ans)
    #print(prepared_data[len(prepared_data)-1])
    return prepared_data

def content_for_sms():
    last_enrty_of_sheet =[0]
    get_dat = get_data_from_sqlite()
    last_enrty_of_sheet = prepare_data_for_sheets(get_dat)
    #print(last_enrty_of_sheet[len(last_enrty_of_sheet)-1])
    return last_enrty_of_sheet[len(last_enrty_of_sheet)-1]
    
def transfer_data_to_google_sheets():
    data_from_sqlite = get_data_from_sqlite()
    data_for_sheets = prepare_data_for_sheets(data_from_sqlite)

    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name(settings.GOOGLE_SHEETS_KEY_FILE, scope)
    client = gspread.authorize(credentials)

    sheet = client.open(settings.GOOGLE_SHEETS_SHEET_NAME)
    worksheet = sheet.get_worksheet(0)

    worksheet.clear()
    worksheet.insert_rows(data_for_sheets)