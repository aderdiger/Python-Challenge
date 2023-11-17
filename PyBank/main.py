# Modules to read in CSV
import os
import csv

csvpath = os.path.join(os.path.dirname(__file__),"Resources","budget_data.csv")

# Lists to store data
month = []
profit_loss = []

# With open as csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read header row
    csvskip = list(next(csvreader))
    csvheader = list(next(csvreader))
    csvlist = list(csvreader)
    
    # Define Lists
    for row in csvlist:
        #  Add month
        month.append(row[0])
        
        # Add profit_loss
        profit_loss.append(int(row[1]))


    # Calculate the total number of months included in the dataset
    total_months = len(month)

    # Calculate the net total amount of "Profit/Losses" over the entire period
    total_profit_loss = sum(profit_loss)
    
    # Loop to calcuate the changes in "Profit/Losses" over the entire period
    profit_change = [profit_loss[i] - profit_loss[i-1] for i in range(len(profit_loss))] 
    
    #And then the average of those changes
    avg_change = round((profit_loss[-1] - profit_loss[0])/ total_months , 2)

    # Calculate he greatest increase in profits (date and amount) over the entire period
    ziplist = dict(zip(month, profit_change))
    max_change = max(profit_change)
    max_month = max(ziplist, key=ziplist.get)

    # Calculate the greatest decrease in profits (date and amount) over the entire period
    min_change = min(profit_change)
    min_month = min(ziplist, key=ziplist.get)

# Print analysis to terminal
    print("Financial Analysis")
    print("-----------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: ${total_profit_loss}")
    print(f"Average Change: ${avg_change}")
    print(f"Greatest Increase in Profits: {max_month} (${max_change})")
    print(f"Greatest Decrease in Profits: {min_month} (${min_change})")

# Export text file with the results
output_file = os.path.join(os.path.dirname(__file__),"Analysis","PyBank Analysis.txt")

f = open(output_file, "w")
f.writelines(["Financial Analysis" + "\n" + 
    "-------------------------------------" + "\n"
    "Total Months: " + str(total_months) + "\n"
    "Total: $" + str(total_profit_loss) + "\n"
    "Average Change: $" + str(avg_change) + "\n"
    "Greatest Increase in Profits: " + str(max_month) + " ($" + str(max_change) + ")" + "\n"
    "Greatest Decrease in Profits: " + str(min_month) + " ($" + str(min_change) + ")"])
f.close()