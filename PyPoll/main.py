"""
* In this challenge, you are tasked with helping a small, rural town modernize
  its vote counting process.

* You will be give a set of poll data called [election_data.csv]
  (PyPoll/Resources/election_data.csv).
  The dataset is composed of three columns: `Voter ID`, `County`, and
  `Candidate`. Your task is to create a Python script that analyzes the votes
  and calculates each of the following:

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

* In addition, your final script should both print the analysis to the
  terminal and export a text file with the results.
"""

# Import required modules
import os
import csv

# Define input and output file paths
input_path = os.path.join("Resources", "election_data.csv")
output_path = os.path.join("analysis", "Election_Results.txt")

vote_count = 0
votes = dict()


with open(input_path) as csv_file:
  csv_reader = csv.reader(csv_file, delimiter=',')
  csv_header = next(csv_reader)
  for row in csv_reader:
    vote_count += 1
    vote_getter = row[2]
    if vote_getter in votes:
        votes[vote_getter] += 1
    else:
        votes[vote_getter] = 1

max_votes = 0

with open(output_path,'w') as txt_file:

    txt_file.write("Election Results\n")
    print("Election Results")

    txt_file.write("----------------------------\n")
    print("----------------------------")

    txt_file.write(f"Total Votes: {vote_count:,}\n")
    print(f"Total Votes: {vote_count:,}")

    txt_file.write("----------------------------\n")
    print("----------------------------")

    for vote_getter in votes:
        votePct = (votes[vote_getter] / vote_count) * 100
        txt_file.write(f"{vote_getter}: {votePct:.3f}% ({votes[vote_getter]:,})\n")
        print(f"{vote_getter}: {votePct:.3f}% ({votes[vote_getter]:,})")
        if votes[vote_getter] > max_votes:
            max_votes = votes[vote_getter]
            winner = vote_getter

    txt_file.write("----------------------------\n")
    print("----------------------------")

    txt_file.write(f"Winner: {winner}\n")
    print(f"Winner: {winner}")

    txt_file.write("----------------------------\n")
    print("----------------------------")

    txt_file.write("---\n")
    print("---")
