import os
import csv

csvpath = os.path.join("Resources", "election_data.csv")
#set variables to store values and dictionaries to hold value keypairs
Counter = 0
Candidatelist = []
votecount = []





with open(csvpath, newline="") as electioncsv:
    csvreader = csv.reader(electioncsv, delimiter=",")
    csvheader = next(electioncsv)
    #print(csvheader) <Verify that the file read in correctly and the header appears as Voter ID, County, Candidate

    for row in csvreader:
        Counter = (Counter + 1) # Tick the counter up for every row in the dataset
        #print(Counter) < Woah this data set is long lol
        candidatename = row[2]
        #print(candidatename)
        if candidatename in Candidatelist:
            candidateid = Candidatelist.index(candidatename)
            votecount[candidateid] = votecount[candidateid] + 1



        #add a new candidate each time we come accross a new value in column 2 then add one vote- Should loop to the above if once the candidate is appended  
        else:
            Candidatelist.append(candidatename)
            votecount.append(1) 
#print(Candidatelist) Make sure the list added all 4 candidates once
#print(votecount) < Check to see if votes are counted seperately for each candidate (SUCESS)     

#Make each percent based on the index in our votecounts and total equaling our final counter
Khanpercent = round(((votecount[0])/ Counter) *100, 2)
Correypercent = round(((votecount[1])/ Counter) *100, 2)
Lipercent = round(((votecount[2])/ Counter) *100, 2)
Otooleypercent = round(((votecount[3])/ Counter) *100, 2) 

#print our results making sure to use strings because my formatted strings werent working
print("Election Results")
print("----------------------------")
print("Total Votes: " + str(Counter))
print("----------------------------")
print("Khan: " + str(Khanpercent) + " % " + str(votecount[0] ))
print("Correy: " + str(Correypercent) + " % " + str(votecount[1] ))
print("Li: " + str(Lipercent) + " % " + str(votecount[2] ))
print("O'Tooley: " + str(Otooleypercent) + " % " + str(votecount[3] ))
print("----------------------------")
print("Winner: Khan")
print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

#Export/Write the code onto a new text file
textpath = os.path.join("Analysis" , "PollingAnalysis.txt")

with open(textpath, "w") as output:
    output.write("Election Results\n")
    output.write("----------------------------\n")
    output.write("Total Votes: " + str(Counter) + "\n")
    output.write("----------------------------\n")
    output.write("Khan: " + str(Khanpercent) + " % " + (str(votecount[0]) + "\n" ))
    output.write("Correy: " + str(Correypercent) + " % " + (str(votecount[1]) + "\n" ))
    output.write("Li: " + str(Lipercent) + " % " + (str(votecount[2]) + "\n" ))
    output.write("O'Tooley: " + str(Otooleypercent) + " % " + (str(votecount[3]) + "\n" ))
    output.write("----------------------------\n")
    output.write("Winner: Khan\n")
    output.write("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")


