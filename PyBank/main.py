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
profit =[]
#increase_date = []
#decrease_date = []
date = []
initial_profit = 0
final_profit = 0 
total_change_profits = 0
monthly_changes = []

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
        
        total_NR += int(row[1])
        profit = row[1]
        final_profit = int(row[1])
        monthly_change_profits = final_profit - initial_profit
        monthly_changes.append(monthly_change_profits)
        total_change_profits = total_change_profits + monthly_change_profits
        initial_profit = final_profit
        count +=1
        average_change_profits = (total_change_profits/count)
        greatest_increase_profits = max(monthly_changes)
        greatest_decrease_profits = min(monthly_changes)
        #increase_date = date[monthly_changes.index(greatest_increase_profits)]
        #decrease_date = date[monthly_changes.index(greatest_decrease_profits)]

            
       
print("Financial Analysis")
print("------------------------------------")
print("Total Months: " + str(count))
print("Total: $" + str(total_NR))
print("Average Change: " + "$" + str(int(average_change_profits)))
print("Greatest Increase in Profits:  $" + str(greatest_increase_profits) )
print("Greatest Decrease in Profits: $"  + str(greatest_decrease_profits) )
print("------------------------------------")