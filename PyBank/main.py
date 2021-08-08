# First we'll import the os module
# This will allow us to create file paths across operating systems
import os
from pathlib import Path

# Module for reading CSV files
import csv
#from typing import NoReturn

#csvpath = os.path.join('.', 'Resources', 'budget_data.csv')
csvpath = Path('./Resources/budget_data.csv')

# Lists to store data
total_NR = 0
date_list =[]
amount_list =[]
with open(csvpath, "r") as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    count = 0
    
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header

    for row in csvreader: 
        if count >=0:
            #print (row)
            total_NR += int(row[1])
            amount_list = row[1]
            print(amount_list)
        count +=1 

print("Total Months: " + str(count))
print("Total: $" + str(total_NR))
print("Average Change: $" + str(total_NR/count))
print("Greatest Increase in Profits:" + str(max(amount_list)))