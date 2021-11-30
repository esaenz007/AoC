# This file builds out the folder structure AoC
# This file also takes in a year as an argument.  If no year is supplied, the current year is used.

import asyncio
from datetime import date
import os
import sys

async def main():

    year = str(date.today().year) # Current year
    xmas_day = 25 # Last day of xmas
    day_of_xmas = 1 # First day of xmas
    parts_per_day = 2 # Number of parts per day

    # Check if year was supplied
    args = sys.argv[1:]
    if len(args) > 0:
        if args[0].isnumeric():
            year = args[0]
        else:
            print("First argument must by a year.")
            return 0

    # Create folder for this years Advent of Code
    print("Creating this years directory...")
    if not os.path.exists(year):
        os.makedirs(year)
        print("Directory created.")
    else:
        print("Directory already exists.")

    
    # Create daily folder
    print("Creating daily folders...")
    for x in range(day_of_xmas, xmas_day + 1):
        daily_folder = os.path.join(year,str(x).zfill(2))
        if not os.path.exists(daily_folder):
            os.makedirs(daily_folder)
            print(f"{daily_folder} created.")
        else:
            print(f"{daily_folder} already exists.")


if __name__ == "__main__":
    asyncio.run(main())