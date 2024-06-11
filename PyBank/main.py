import os
import csv

# Define the path to the CSV file
csvpath = os.path.join("Resources", "budget_data.csv")

# Initialize variables
total_months = 0
total_profit_loss = 0
previous_profit_loss = 0
profit_loss_changes = []
months = []

# Read the CSV file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # Skip the header
    header = next(csvreader)
    
    # Process the data
    for row in csvreader:
        # Track the total number of months
        total_months += 1
        # Track the net total amount of "Profit/Losses" over the entire period
        total_profit_loss += int(row[1])
        
        # Track changes in "Profit/Losses"
        if total_months > 1:
            profit_loss_change = int(row[1]) - previous_profit_loss
            profit_loss_changes.append(profit_loss_change)
            months.append(row[0])
        
        previous_profit_loss = int(row[1])

# Calculate average change
average_change = sum(profit_loss_changes) / len(profit_loss_changes)

# Calculate greatest increase and decrease
greatest_increase = max(profit_loss_changes)
greatest_decrease = min(profit_loss_changes)
greatest_increase_month = months[profit_loss_changes.index(greatest_increase)]
greatest_decrease_month = months[profit_loss_changes.index(greatest_decrease)]

# Print the analysis
analysis = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_profit_loss}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n"
    f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})\n"
)

print(analysis)

# Save the analysis to a text file
output_path = os.path.join("analysis", "results.txt")
os.makedirs("analysis", exist_ok=True)
with open(output_path, "w") as txtfile:
    txtfile.write(analysis)


