#import modules needed
import os
import csv
#set read filepath
budgetDataCSV = os.path.join("Resources", "budget_data.csv")
#create file wrapper
with open(budgetDataCSV, 'r') as csvFile:
    #create file reader
    csvReader = csv.reader(csvFile, delimiter=",")
    #file header as list
    header = next(csvReader)
    #file first row of data as list
    initials = next(csvReader)
    #initialize data collecting variables
    totalMonths = 1
    totalProfit = int(initials[1])
    previousRow = int(initials[1])
    changesList = []
    greatestIncrease = [initials[0], int(initials[1])]
    greatestDecrease = [initials[0], int(initials[1])]

    for row in csvReader:
        totalMonths += 1
        totalProfit += int(row[1])
        changeFromLast = int(row[1])-previousRow
        changesList.append(changeFromLast)
        previousRow = int(row[1])
        if changeFromLast > greatestIncrease[1]:
            greatestIncrease[0] = row[0]
            greatestIncrease[1] = changeFromLast
        if changeFromLast < greatestDecrease[1]:
            greatestDecrease[0] = row[0]
            greatestDecrease[1] = changeFromLast
        
print("Financial Analysis\n")
print("----------------------------\n")
print(f"Total Months: {totalMonths}\n")
print(f"Total: ${totalProfit}\n")
averageChange = sum(changesList) / len(changesList)
print(f"Average Change: ${averageChange:.2f}\n")
print(f"Greatest Increase in Profits: {greatestIncrease[0]} (${greatestIncrease[1]})\n")
print(f"Greatest Decrease in Profits: {greatestDecrease[0]} (${greatestDecrease[1]})\n")

analysisTXT = os.path.join("analysis", "PyBank Analysis.txt")
with open(analysisTXT, 'w') as txtFile:
     
    txtFile.write("Financial Analysis\n")
    txtFile.write("----------------------------\n")
    txtFile.write(f"Total Months: {totalMonths}\n")
    txtFile.write(f"Total: ${totalProfit}\n")
    txtFile.write(f"Average Change: ${averageChange:.2f}\n")
    txtFile.write(f"Greatest Increase in Profits: {greatestIncrease[0]} (${greatestIncrease[1]})\n")
    txtFile.write(f"Greatest Decrease in Profits: {greatestDecrease[0]} (${greatestDecrease[1]})\n")
