import os
import csv
csvpath = os.path.join('..', 'Resources', 'election_data.csv')
outpath=os.path.join('output.txt')
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
        a=round(((votesforeach[row]/voteCounter)*100), 2)
        votesforeachp.append(a)

    for row in range(len(votesforeach)):
        winner= votesforeach[0]
        if winner<= votesforeach[row]:
            winner=uniquecandidates[row]
        else:
            winner=uniquecandidates[0]
        

    

with open(outpath,'w') as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("-----------------------------\n")
    txtfile.write(f"Total Votes {voteCounter} \n")
    txtfile.write("-----------------------------\n")
    txtfile.write(f"{uniquecandidates[0]} : {votesforeachp[0]} % ({votesforeach[0]})\n")
    txtfile.write(f"{uniquecandidates[1]} : {votesforeachp[1]} % ({votesforeach[1]})\n")
    txtfile.write(f"{uniquecandidates[2]} : {votesforeachp[2]} % ({votesforeach[2]})\n")
    txtfile.write(f"{uniquecandidates[3]} : {votesforeachp[3]} % ({votesforeach[3]})\n")
    txtfile.write(f"{uniquecandidates[4]} : {votesforeachp[4]} % ({votesforeach[4]})\n")
    txtfile.write("-------------------------------\n")
    txtfile.write(f"Winner : {winner}\n")
    txtfile.write("--------------------------------\n")


print("Election Results")
print("-----------------------------")
print(f"Total Votes {voteCounter} ")
print("-----------------------------")
for x in range(len(uniquecandidates)):
    print(f"{uniquecandidates[x]} : {votesforeachp[x]} % ({votesforeach[x]})")
print("-------------------------------")
print(f"Winner : {winner}")
print("--------------------------------")







        
