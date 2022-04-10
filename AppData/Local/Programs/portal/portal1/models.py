from __future__ import print_function
# from inspect import EndOfBlock
from django.db import models
# from gsheets import mixins
# from uuid import uuid4

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from pprint import pprint

from googleapiclient import discovery


SCOPES = [
'https://www.googleapis.com/auth/spreadsheets',
'https://www.googleapis.com/auth/drive',
 'https://www.googleapis.com/auth/drive.file'
]
SAMPLE_SPREADSHEET_ID = '19gjDr7M0k7K9Tb4f1xL4wMUIZ7__5ZOmUOqHbhgexuY'


# class portal1(mixins.SheetSyncableMixin, models.Model): #SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# If modifying these scopes, delete the file token.json.

# The ID and range of a sample spreadsheet.
#write=[[1,1,"frak",1,1],]
write=[]
class portal1(models.Model):
    
    billID = models.AutoField(primary_key = True)
    rollno = models.IntegerField()
    name = models.CharField(max_length = 200)
    invoiceno = models.IntegerField()
    indentno = models.IntegerField()
    bill = models.FileField(upload_to = 'uploads/' )


  
    write=[rollno,name,invoiceno,indentno]
        
    
    
 

creds = None
creds = Credentials.from_authorized_user_file('token.json', SCOPES)
        # The file token.json stores the user 's access and refresh tokens, and is#
        # created automatically when the authorization flow completes
        # for the first# time.

    # HELLO
    # if os.path.exists('token.json'):
    #     creds = Credentials.from_authorized_user_file('token.json', SCOPES)# If there are no(valid) credentials available,
    #     #let the user log in .
    # if not creds or not creds.valid:
    #     if creds and creds.expired and creds.refresh_token:
    #         creds.refresh(Request())
    #     else :
    #         flow = InstalledAppFlow.from_client_secrets_file('portal1\credentials.json', SCOPES)
    #         creds = flow.run_local_server(port = 0)
    #         # Save the credentials for the next run
    #     with open('token.json', 'w') as token:
    #         token.write(creds.to_json())
    # BYE

try:
    service1= build('sheets', 'v4', credentials = creds)
    
    service = discovery.build('sheets', 'v4', credentials = creds)
    #print(service)
# Call the Sheets API
    sheet = service1.spreadsheets()
    # result = sheet.values().get(spreadsheetId = SAMPLE_SPREADSHEET_ID, range = "Sheet1!A1:E3").execute()
    # print(result)
    sheet1=service.spreadsheets()
    request = sheet1.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range='Sheet1!B4:E4', valueInputOption='USER_ENTERED', body={"values":write}).execute()
    
    # form = user_form(request.POST)
    # data = form.save(commit=False)
    # print(data)
    
    print(request)
    pprint(request)

except HttpError as err: 
    print(err)

# ## ""
# "Shows basic usage of the Sheets API.##
# Prints values from a sample spreadsheet.##
# ""
# "#

# except HttpError as err: #print(err)

        
    

