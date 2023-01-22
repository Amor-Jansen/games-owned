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


def main_menu():
    """
    The main menu will promt the user on what sheet they want to access.
    As well as exit options.
    """
    print('What would you like to do?')
    print('Please select 1 - 4')
    print('1. ps4\n 2. ps3\n 3. New Entry\n 4. Quit')

    while True:
        list_choice = input('What would you like to do: \n')

        if list_choice == '1':
            print('Welcome to the ps4 list')
            break
        elif list_choice == '2':
            print('welcome to the ps3 list')
            break
        elif list_choice == '3':
            print('A new game? Lets add it!')
            break
        elif list_choice == '4':
            print('See you next time!')
            quit()
        else:
            print('Invalid! Choose 1-4 please!')

    main_menu()