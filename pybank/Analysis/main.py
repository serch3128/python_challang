import os
import csv
csvpath = os.path.join('..', 'Resources', '02-Homework_03-Python_Instructions_PyBank_Resources_budget_data.csv')
outpath=os.path.join('output.txt')
totalMonth=[]
totalProfit=[]
change=[]

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    for row in csvreader:
        totalMonth.append(row[0])
        totalProfit.append(int(row[1]))

    totalMonths= len(totalMonth)
    ProfitsLosses = 0
    difference=0
  
    for x in range(len(totalProfit)):
        ProfitsLosses=ProfitsLosses+totalProfit[x]
        
    for x in range(len(totalProfit)-1):   
        difference = totalProfit[x+1]-totalProfit[x]
        change.append(difference)

    sumchange = 0    

    for x in range(len(change)):
        sumchange=sumchange+change[x]
    
    gretIncr=0
    monthIncr=0
    gretDecr=0
    monthDecr=0

    for x in range(len(totalProfit)):
        if totalProfit[x]>=gretIncr:
            gretIncr=totalProfit[x]
            monthIncr=totalMonth[x]
        if totalProfit[x]<gretDecr:
            gretDecr=totalProfit[x]
            monthDecr=totalMonth[x]
       

    
    avgchange= sumchange/(len(change))

with open(outpath,'w') as txtfile:
    txtfile.write("Financial Analysis \n")
    txtfile.write("----------------------------\n")
    txtfile.write(f"Total Months : {totalMonths}\n")
    txtfile.write(f"Total : $ {ProfitsLosses}\n")
    txtfile.write(f"Average Change : $ {avgchange}\n")
    txtfile.write(f"Greatest Increase in Profits: {monthIncr} $ {gretIncr}\n")
    txtfile.write(f"Greatest Decrease in Profits: {monthDecr} $ {gretDecr}\n")

print("Financial Analysis")
print("----------------------------")
print(f"Total Months : {totalMonths}")
print(f"Total : $ {ProfitsLosses}")
print(f"Average Change : $ {avgchange}")
print(f"Greatest Increase in Profits: {monthIncr} $ {gretIncr}")
print(f"Greatest Decrease in Profits: {monthDecr} $ {gretDecr}")


  
   
 
    



    
    
   

   
    

    
