import os
import csv
csvpath = os.path.join('..', 'Resources', 'election_data.csv')
votes=[]
candidates=[]
votesforeach=[0,0,0,0,0]
votesforeachp=[]
uniquecandidates=[]
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)      
    csv_header = next(csvreader)
    

    for row in csvreader:
        votes.append(row[0])
        candidates.append(row[1])

    voteCounter=len(votes)

    for row in candidates:
        if row not in uniquecandidates:
            uniquecandidates.append(row)
        
    for x in range(len(uniquecandidates)):
        for row in candidates: 
            if  row == uniquecandidates[x]:
                votesforeach[x]=votesforeach[x]+1

    for row in range(len(votesforeach)):
        a=votesforeach[row]/voteCounter
        votesforeachp.append(a)

print(votesforeachp)


print("Election Results")
print("-----------------------------")
print(f"Total Votes {voteCounter} ")
print("-----------------------------")



print(votesforeach)


        

print(uniquecandidates) 
        

    




print(len(candidates))



        
