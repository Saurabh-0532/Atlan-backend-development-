# data_transfer.py
import gspread
import logging
from django.conf import settings
from oauth2client.service_account import ServiceAccountCredentials
from .models import Questions, Answer# Replace 'YourModel' with the name of your Django model representing the data you want to transfer

logging.basicConfig(level=logging.INFO)

def get_data_from_sqlite():
    data = Questions.objects.all()  #fetching the values from the index_questions table or from questions model
    return data
def get_data_from_answers():        #fetching the values from the index_answer table or from Answer model
    res = Answer.objects.all()
    return res

def prepare_data_for_sheets(data):
    prepared_data = []
    row = []
    
    for item in data:
        row.append(item.question)  
    prepared_data.append(row)
    ans_obj = get_data_from_answers()
    col_len = 0
    length_row= 0
    ans_len = 0
    
    if len(row)!=0: #only execute if any anwer is recorded
        length_row = len(row)
        ans_len = len(ans_obj)
        col_len = int(len(ans_obj)/length_row) # this is for finding the numbers or responses done 
        k = 0
        # this 'for loop' is used for organising the data so that it can reflect properly in the google sheet
        for j in range(0,col_len):
            ansrow =[] # puthing all answer into a list 
            for i in range(k,len(row)+(j*(len(row)))):
                #print(i)
                ansrow.append(ans_obj[i].answer)
                k += 1       
            prepared_data.append(ansrow)
        return prepared_data
    else:
        prepared_data[0] = 'Error'
        return prepared_data
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