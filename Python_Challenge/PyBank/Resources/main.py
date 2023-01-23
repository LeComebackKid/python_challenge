#import csv
import os
import csv

#add a variable to load a file from a path 
csvpath = "/Users/jdeemo/Desktop/Classwork/Module3 _Python/Instructions/PyBank/Resources/budget_data.csv"

#add variable to save the file to a path
file_to_save = "budget_data_results.txt"

#initialize variables to store data
total_months = 0 
prev_amount = 0 
amount_total = 0 
average_change = 0 
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999]

#create lists to store the months and profits/loses
months = []
profits_loses = []

#read the csv and convert lists to dictionaries
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #read the header
    header = next(csvreader)

    #for each row in the csv file
    for row in csvreader:

        #track the totals
        total_months += 1
        amount_total += float(row[1])


        months = (row[0])

        #track the cash amounts - profits/loses
        monthly_change = float(row[1]) - prev_amount
        prev_amount = float(row[1])
        profits_loses = [prev_amount] + [monthly_change]

        #calculate greatest increase
        if (monthly_change > greatest_increase[1]):
            greatest_increase[1] = monthly_change

        if (monthly_change > greatest_decrease[1]):
            greatest_decrease[1] = monthly_change

average_change = sum(profits_loses)/ len(profits_loses)

#output
budget_data_results = (
    f"\nFinancial Analysis"
    f"\n----------------------------\n"
    f"\nTotal Months: {total_months}\n"
    f"\nTotal: ${amount_total}\n"
    f"\nAverage Change: ${average_change}\n"
    f"\nGreatest Increase in Profits: ${greatest_increase}\n"
    f"\nGreatest Decrease in Profits: ${greatest_decrease}\n"
)

print (budget_data_results)
