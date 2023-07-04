"""
Author: Pete Newman
Date Started: 2023-07-03

Function for uploading swipe access data to google sheets
"""

from decouple import config
import gspread
import json

SPREADSHEET_ID = config("SPREADSHEET_ID")
CHECKIN_SHEET_NAME = "Checkins"


def main():
    print("Authenticating to google sheets")
    with open("auth.json", "r") as file:
        # Load the JSON data into a dictionary
        CREDENTIALS = json.load(file)
    gc = gspread.service_account_from_dict(CREDENTIALS)
    print("Successfully authenticated!")
    print("Opening worksheet")
    sparkhaus_ss = gc.open_by_key(SPREADSHEET_ID)
    print("Successfully opened spreadsheet!")
    print("Opening worksheet...")
    checkin_sheet = sparkhaus_ss.worksheet(CHECKIN_SHEET_NAME)
    print("Successfully opened worksheet!")
    checkin_sheet.append_row(
        ["03/07/2023 16:27:00", "peter.newman.22@gmail.com", "In", False]
    )
    # checkin_sheet.


if __name__ == "__main__":
    main()
