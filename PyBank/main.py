"""
* In this challenge, you are tasked with creating a Python script for
  analyzing the financial records of your company. You will give a set of
  financial data called [budget_data.csv](PyBank/Resources/budget_data.csv).
  The dataset is composed of two columns: `Date` and `Profit/Losses`.
  (Thankfully, your company has rather lax standards for accounting so the
  records are simple.)

* Your task is to create a Python script that analyzes the records to
  calculate each of the following:

  * The total number of months included in the dataset

  * The net total amount of "Profit/Losses" over the entire period

  * Calculate the changes in "Profit/Losses" over the entire period, then find
    the average of those changes

  * The greatest increase in profits (date and amount) over the entire period

  * The greatest decrease in profits (date and amount) over the entire period

* As an example, your analysis should look similar to the one below:

  ```text
  Financial Analysis
  ----------------------------
  Total Months: 86
  Total: $38382578
  Average  Change: $-2315.12
  Greatest Increase in Profits: Feb-2012 ($1926159)
  Greatest Decrease in Profits: Sep-2013 ($-2196167)
  ```

* In addition, your final script should both print the analysis to the
  terminal and export a text file with the results.
"""

# Import required modules
import os
import csv

# Define input and output file paths
input_path = os.path.join("Resources", "budget_data.csv")
output_path = os.path.join("analysis", "Financial_Analysis.txt")

# Set up variable initial values
month_count = 0
total_net_profit = 0
max_increase = 0
max_decrease = 0
first_month = True
total_change = 0

# Open input file and step through data
with open(input_path) as csv_file:

  csv_reader = csv.reader(csv_file, delimiter=',')
  
  # Read header row - not used in calculations
  csv_header = next(csv_reader)
  
  # Step through data rows
  for row in csv_reader:                             # Read the current data row
    month_count += 1                                 # Increment month counter
    current_month = int(row[1])                      # Get profit / loss for current month
    total_net_profit += current_month                # Add it to the net profit accumulator
  
    if first_month == True:                          # Skip max increase / decrease calcs for 1st month
      first_month = False                            # Not the first month anymore
    else:
      total_change += (current_month - prev_month)   # Accumulate total monthly change
      if total_change > max_increase:                # Check for new max increase
        max_increase = total_change
        max_inc_month = row[0]
      if total_change < max_decrease:                # Check for new max decrease
        max_decrease = total_change
        max_dec_month = row[0]
    prev_month = current_month                       # Set new previouse monthe value for next time through

# Open output file and write results to both file and console
with open(output_path,'w') as txt_file:

  txt_file.write("Financial Analysis\n")
  print("Financial Analysis")

  txt_file.write("----------------------------\n")
  print("----------------------------")

  txt_file.write(f"Total Months: {month_count}\n")
  print(f"Total Months: {month_count}")

  txt_file.write(f"Total Net Profit: ${total_net_profit:,.2f}\n")
  print(f"Total Net Profit: ${total_net_profit:,.2f}")

  txt_file.write(f"Total Period Change in Profit: ${total_change:,.2f}\n")
  print(f"Total Period Change in Profit: ${total_change:,.2f}")

  # Calculate average change in profit
  txt_file.write(f"Average Change in Profit: ${total_change/(month_count-1):,.2f}\n")
  print(f"Average Change in Profit: ${total_change/(month_count-1):,.2f}")

  txt_file.write(f"Greatest Increase in Profits: {max_inc_month} (${max_increase:,.2f})\n")
  print(f"Greatest Increase in Profits: {max_inc_month} (${max_increase:,.2f})")

  txt_file.write(f"Greatest Decrease in Profits: {max_dec_month} (${max_decrease:,.2f})\n")
  print(f"Greatest Decrease in Profits: {max_dec_month} (${max_decrease:,.2f})")

  txt_file.write("---\n")
  print("---")
