import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('games_owned')

ps4 = SHEET.worksheet('ps4')
ps3 = SHEET.worksheet('ps3')

# Welcome message

print('Welcome to your games owned list.')
print('Here you can view all the \n video games you own.')
print('You can also update your list.')
print('To make sure you do not buy doubles. \n')

# Name request

print('Please enter your name.')
print('It must be a valid name at least 8 characters long.')
print('only A-z, a-z and 0-8 will be accepted')
print('Blank space will be removed')
