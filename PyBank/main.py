
import os, csv


budget_file_path = os.path.join("PyBank/Resources/budget_data.csv")


# --------------------------------------------------------------------------
# Created empty lists to store future values of months, profits, and monthly profit change.
# --------------------------------------------------------------------------

total_months = []
total_profit = []
monthly_profit_change = []


# --------------------------------------------------------------------------
# Opened the csv file and defined it as the 'budget_file' variable. 
# Read through the csv data and store the data within the 'budget_data' variable. 
# Skipped the header of the csv file to ensure clean data.
# --------------------------------------------------------------------------
 
with open(budget_file_path) as budget_file:
    budget_data = csv.reader(budget_file) 
    next(budget_data)  


# --------------------------------------------------------------------------
# Went through the rows of the csv file and added the month/profit to the list for each defined variable
# --------------------------------------------------------------------------

    for row in budget_data: 
        total_months.append(row[0])
        total_profit.append(int(row[1]))


# --------------------------------------------------------------------------
# Found the full range of the total profits csv, calculate the monthly change in profits, and added the calculations to the 'monthly_profit_change' list
# --------------------------------------------------------------------------

    for i in range(len(total_profit)-1):
        monthly_profit_change.append(total_profit[i+1]-total_profit[i])

        
# --------------------------------------------------------------------------
# Found the greatest increase in profits (max) and the greatest decrease in profits (min) from the monthly_profit_change
# --------------------------------------------------------------------------        

max_increase_value = max(monthly_profit_change)
max_decrease_value = min(monthly_profit_change)


# --------------------------------------------------------------------------
# Calculated the index number for the month associated with the greatest increase/decrease. 
# Had to add '+1' because the end result was printing the month before the correct month.
# --------------------------------------------------------------------------

max_increase_month = monthly_profit_change.index(max(monthly_profit_change)) + 1
max_decrease_month = monthly_profit_change.index(min(monthly_profit_change)) + 1 


# --------------------------------------------------------------------------
# Printed out the results to the terminal
# --------------------------------------------------------------------------

print("Financial Analysis")
print("----------------------------")
# print out total amount of months in the 'total_months' list
print(f"Total Months: {len(total_months)}")
# add up all the amounts from the 'total_profits' list and print it out
print(f"Total: ${sum(total_profit)}")
# find the average change by dividing the sum of all monthly changes by the amount of monthly changes in the 'monthly_profit_change' list. Make sure it is rounded to 2 decimals.
print(f"Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
# print out the month corresponding to the index number found with 'max_increase/decrease_month' and print out the value.
print(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
print(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")


# --------------------------------------------------------------------------
# Created a text file for the results. Learned to add "\n" to create a new line.
# --------------------------------------------------------------------------

results = os.path.join("PyBank/Analysis/budget_results.csv")
with open(results,"w") as file:
    file.write("Financial Analysis")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Total Months: {len(total_months)}")
    file.write(" ")
    file.write(f"Total: ${sum(total_profit)}")
    file.write("\n")
    file.write(f"Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")



