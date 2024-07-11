import os
import csv

# Path to budget data CSV file
budget_data_csv = os.path.join('PyBank', 'Resources', 'budget_data.csv')

# Initialize variables
total_months = 0
total_profit_loss = 0
previous_profit_loss = 0
monthly_changes = []
months = []

# Open and read CSV file
with open(budget_data_csv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # Skip header row
    csv_header = next(csvreader)
    
    # Loop through rows in CSV
    for row in csvreader:
        # Count total months
        total_months += 1
        
        # Calculate total profit/loss
        total_profit_loss += int(row[1])
        
        # Track months and profit/loss for calculating changes
        months.append(row[0])
        current_profit_loss = int(row[1])
        
        # Calculate monthly change and store in list
        if total_months > 1:
            monthly_change = current_profit_loss - previous_profit_loss
            monthly_changes.append(monthly_change)
        
        # Update previous profit/loss for next iteration
        previous_profit_loss = current_profit_loss

# Calculate average change
average_change = sum(monthly_changes) / len(monthly_changes)

# Find greatest increase and decrease in profits
greatest_increase = max(monthly_changes)
greatest_decrease = min(monthly_changes)

# Find corresponding month for greatest increase and decrease
increase_month = months[monthly_changes.index(greatest_increase) + 1]
decrease_month = months[monthly_changes.index(greatest_decrease) + 1]

# Print financial analysis
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit_loss}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {increase_month} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {decrease_month} (${greatest_decrease})")

# Write financial analysis to a text file
output_file = os.path.join('PyBank', 'Analysis', 'financial_analysis.txt')
with open(output_file, 'w') as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("----------------------------\n")
    txtfile.write(f"Total Months: {total_months}\n")
    txtfile.write(f"Total: ${total_profit_loss}\n")
    txtfile.write(f"Average Change: ${average_change:.2f}\n")
    txtfile.write(f"Greatest Increase in Profits: {increase_month} (${greatest_increase})\n")
    txtfile.write(f"Greatest Decrease in Profits: {decrease_month} (${greatest_decrease})\n")
