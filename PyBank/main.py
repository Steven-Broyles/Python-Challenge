import os
import csv

#Get correct file path
csvpath = os.path.join("Resources" , "budgetdata.csv")

#Set two variables for holding info needed later for calculations and set all other variables to 0 before the for loop
months = []
changesinprofit = []

monthcount = 0
monthlychange = 0
nowprofit = 0
previousprofit = 0
totalprofitloss = 0





with open(csvpath, newline="") as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")
    #define and move past the header
    csvheader = next(csvfile)

   
    for row in  csvreader:
    
        monthcount += 1 

        nowprofit = int(row[1])
        totalprofitloss += nowprofit

        #print(nowprofit) < Verify we are getting integer values representing the profit/loss line in csv
        #print(totalprofitloss)  < Verify the counter is ticking rows and summing correctly
        if (monthcount ==1):
                #
           previousprofit = nowprofit
           continue
        else:

            monthlychange = nowprofit - previousprofit

            #store in variables made above
            changesinprofit.append(monthlychange)
            months.append(row[0])
            #then reset for the loop to see a new row of values and changes
            previousprofit = nowprofit
            #print(monthlychange) < Verify the monthly changes in profit and loss are accurate and printing row by row
            #print(monthcount) < Verify the month couter ticks to a total of 86 which matches the total number of data points
sumofchanges = sum(changesinprofit)
averageofprofits = (sumofchanges) / (monthcount - 1)
#print(averageofprofits) #< Verify that this matches Our first value(867994) minus (671099) divided by the number of entries -1(MINUS 1 BECAUSE 85 CHANGES between 86 values *AHAAAA Moment*) 
#find the values ascociated with the highest and lowest changes from our set
highestchange = max(changesinprofit)
lowestchange = min(changesinprofit)
#locate which index they correspond with to match up to the month column for "Best and Worst months"
highestchangepoint = changesinprofit.index(highestchange) # 24
lowestchangepoint = changesinprofit.index(lowestchange) # 43

bestmonth = months[highestchangepoint]
worstmonth = months[lowestchangepoint] 
#Print the statements we want to appear to the terminal
print("Financial Analysis")
print("---------------------")
print(f"Total Months: {monthcount}")
print(f"Total Profits/Losses: {totalprofitloss}")
print(f"Average Change: {averageofprofits}")
print(f"Best Month (Greatest Profit Increase) : {bestmonth} (${highestchange})")
print(f"Worst Month (Greatest Profit Decrease) : {worstmonth} (${lowestchange})")



textpath= os.path.join("Analysis", "BudgetAnalysis.txt")

with open(textpath, "w") as output:
#This part we didnt cover too thouroughly or I missed something along the way- Google was a huge help
    output.write("Financial Analysis\n")
    output.write("---------------------\n")
    output.write(f"Total Months: {monthcount}\n")
    output.write(f"Total Profits/Losses: {totalprofitloss}\n")
    output.write(f"Average Change: {averageofprofits}\n")
    output.write(f"Best Month (Greatest Profit Increase) : {bestmonth} (${highestchange})\n")
    output.write(f"Worst Month (Greatest Profit Decrease) : {worstmonth} (${lowestchange})")