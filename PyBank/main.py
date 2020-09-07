import os
import csv

pybank = os.path.join("Resources", "budget_data.csv")

with open(pybank, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

def financial_analysis(pybank):
    date = str(pybank[0])
    profit_loss = int(pybank[1])

    months = 
    total = sum(profit_loss)
    average_pl = sum(profit_loss) / len(profit_loss)
    increase = 
    decrease = 

    print(f"Financial Analysis")
    print(f"----------------------------")
    print(f"Total Months: {str(months)}")
    print(f"Total: {str(total)}")
    print(f"Average Change: {str(average_pl)}")
    print(f"Greatest Increase in Profits: {str(increase)}")
    print(f"Greatest Decrease in Profits: {str(decrease)}")
