"""
* In this challenge, you are tasked with creating a Python script for analyzing the financial records of your company. You will give a set of financial data called [budget_data.csv](PyBank/Resources/budget_data.csv). The dataset is composed of two columns: `Date` and `Profit/Losses`. (Thankfully, your company has rather lax standards for accounting so the records are simple.)

* Your task is to create a Python script that analyzes the records to calculate each of the following:

  * The total number of months included in the dataset

  * The net total amount of "Profit/Losses" over the entire period

  * Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes

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

* In addition, your final script should both print the analysis to the terminal and export a text file with the results.
"""
import os
import csv

inputPath = os.path.join("Resources", "budget_data.csv")
outputPath = os.path.join("analysis", "Financial_Analysis.txt")

rowCount = 0
monthCount = 0
totalNetProfit = 0
maxIncrease = 0
maxDecrease = 0
firstMonth = True
firstProfitLoss = 0
totalChange = 0
prevMonth = 0
currentMonth = 0

with open(inputPath) as csvFile:
  csvReader = csv.reader(csvFile, delimiter=',')
  csvHeader = next(csvReader)
  for row in csvReader:
    monthCount += 1
    currentMonth = int(row[1])
    totalNetProfit += currentMonth
    if firstMonth == True:
      firstMonth = False
    else:
      totalChange += (currentMonth - prevMonth)
      if totalChange > maxIncrease:
        maxIncrease = totalChange
        maxIncMonth = row[0]
      if totalChange < maxDecrease:
        maxDecrease = totalChange
        maxDecMonth = row[0]
    prevMonth = currentMonth

with open(outputPath,'w') as txtFile:
  txtFile.write("Financial Analysis\n")
  print("Financial Analysis")
  txtFile.write("----------------------------\n")
  print("----------------------------")
  txtFile.write(f"Total Months: {monthCount}\n")
  print(f"Total Months: {monthCount}")
  txtFile.write(f"Total Net Profit: ${totalNetProfit:,.2f}\n")
  print(f"Total Net Profit: ${totalNetProfit:,.2f}")
  txtFile.write(f"Total Period Change in Profit: ${totalChange:,.2f}\n")
  print(f"Total Period Change in Profit: ${totalChange:,.2f}")
  txtFile.write(f"Average Change in Profit: ${totalChange/(monthCount-1):,.2f}\n")
  print(f"Average Change in Profit: ${totalChange/(monthCount-1):,.2f}")
  txtFile.write(f"Greatest Increase in Profits: {maxIncMonth} (${maxIncrease:,.2f})\n")
  print(f"Greatest Increase in Profits: {maxIncMonth} (${maxIncrease:,.2f})")
  txtFile.write(f"Greatest Decrease in Profits: {maxDecMonth} (${maxDecrease:,.2f})\n")
  print(f"Greatest Decrease in Profits: {maxDecMonth} (${maxDecrease:,.2f})")
  txtFile.write("---\n")
  print("---")

