"""
* In this challenge, you are tasked with helping a small, rural town modernize its vote counting process.

* You will be give a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv).
The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. Your task is to create 
a Python script that analyzes the votes and calculates each of the following:

  * The total number of votes cast

  * A complete list of candidates who received votes

  * The percentage of votes each candidate won

  * The total number of votes each candidate won

  * The winner of the election based on popular vote.

* As an example, your analysis should look similar to the one below:

  ```text
  Election Results
  -------------------------
  Total Votes: 3521001
  -------------------------
  Khan: 63.000% (2218231)
  Correy: 20.000% (704200)
  Li: 14.000% (492940)
  O'Tooley: 3.000% (105630)
  -------------------------
  Winner: Khan
  -------------------------
  ```

* In addition, your final script should both print the analysis to the terminal and export a text file
with the results.
"""

import os
import csv

inputPath = os.path.join("Resources", "election_data.csv")
outputPath = os.path.join("analysis", "Election_Results.txt")

voteCount = 0
votes = dict()


with open(inputPath) as csvFile:
  csvReader = csv.reader(csvFile, delimiter=',')
  csvHeader = next(csvReader)
  for row in csvReader:
    voteCount += 1
    voteGetter = row[2]
    if voteGetter in votes:
        votes[voteGetter] += 1
    else:
        votes[voteGetter] = 1

maxVotes = 0
winner = ""

with open(outputPath,'w') as txtFile:
    txtFile.write("Election Results\n")
    print("Election Results")
    txtFile.write("----------------------------\n")
    print("----------------------------")
    txtFile.write(f"Total Votes: {voteCount:,}\n")
    print(f"Total Votes: {voteCount:,}")
    txtFile.write("----------------------------\n")
    print("----------------------------")
    for voteGetter in votes:
        votePct = (votes[voteGetter] / voteCount) * 100
        txtFile.write(f"{voteGetter}: {votePct:.3f}% ({votes[voteGetter]:,})\n")
        print(f"{voteGetter}: {votePct:.3f}% ({votes[voteGetter]:,})")
        if votes[voteGetter] > maxVotes:
            maxVotes = votes[voteGetter]
            winner = voteGetter
    txtFile.write("----------------------------\n")
    print("----------------------------")
    txtFile.write(f"Winner: {winner}\n")
    print(f"Winner: {winner}")
    txtFile.write("----------------------------\n")
    print("----------------------------")
    txtFile.write("---\n")
    print("---")
        

"""
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
"""
