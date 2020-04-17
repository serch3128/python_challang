import os
import csv
csvpath = os.path.join('..', 'Resources', '02-Homework_03-Python_Instructions_PyPoll_Resources_election_data.csv')
votes=[]
candidates=[]
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)      
    csv_header = next(csvreader)
    

    for row in csvreader:
        votes.append(row[0])

voteCounter=len(votes)
print(voteCounter)

    for row in range(1,votecounter):
        candidates.append(csvfile[row])
    
    print(candidates)
        
