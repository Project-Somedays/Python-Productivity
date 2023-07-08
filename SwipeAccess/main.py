"""
Author: Pete Newman
Date Started: 2023-07-03

Function for uploading swipe access data to google sheets
"""


import gspread
import json
import logging
from datetime import datetime
from pprint import pprint
from decouple import config

logger = logging.getLogger("test")
logger.setLevel(level=logging.DEBUG)

logFileFormatter = logging.Formatter(
    fmt=f"%(levelname)s %(asctime)s \t %(funcName)s L%(lineno)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
fileHandler = logging.FileHandler(filename="test.log", mode="w")
fileHandler.setFormatter(logFileFormatter)
fileHandler.setLevel(level=logging.INFO)

logger.addHandler(fileHandler)

SPREADSHEET_ID = config("SPREADSHEET_ID")
CHECKIN_SHEET_NAME = "Checkins"
TESTCASE = "peter.newman.22@gmail.com"
DATETIMEFORMAT = "%d/%m/%Y %H:%M:%S"


def main():
    logger.info("Authenticating to google sheets")
    with open(file="auth.json", mode="r", encoding="utf-8") as file:
        # Load the JSON data into a dictionary
        credentials = json.load(file)
    gc = gspread.service_account_from_dict(credentials)
    logger.info("Successfully authenticated!")
    logger.info("Opening worksheet")
    sparkhaus_ss = gc.open_by_key(SPREADSHEET_ID)
    logger.info("Successfully opened spreadsheet!")
    logger.info("Opening worksheet...")
    checkin_sheet = sparkhaus_ss.worksheet(CHECKIN_SHEET_NAME)
    logger.info("Successfully opened worksheet!")

    logger.info("Loading in the previous 100 entries")
    last_row = checkin_sheet.row_count
    first_row = max(last_row - 100, 2)
    logger.info(f"First row: {first_row}, Last row: {last_row}")
    last_hundred_rows = checkin_sheet.get(f"A{first_row}:D{last_row}")

    relevant_rows = [
        r
        for r in last_hundred_rows
        if r[1] == TESTCASE
        and datetime.strptime(r[0], DATETIMEFORMAT).date() == datetime.today().date()
    ]

    # pprint(relevant_rows)
    sign_in_or_out = (
        "In" if (len(relevant_rows) == 0 or relevant_rows[-1][2] == "Out") else "Out"
    )

    checkin_sheet.append_row(
        [
            datetime.strftime(datetime.now(), "%d/%m/%Y %H:%M:%S"),
            TESTCASE,
            sign_in_or_out,
            False,
        ]
    )

    # all_data = checkin_sheet.get_all_values()

    # pprint(all_data)


if __name__ == "__main__":
    main()
