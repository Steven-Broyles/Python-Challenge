#import dependencies
import os
import csv
#Get correct file path
csvpath = os.path.join("/Resources/budgetdata.csv")
with open(csvpath, newline="") as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")

    print(csvreader)


