# Place code below to do the analysis part of the assignment.

import csv

with open('clean_data.csv', 'r') as file:
    reader = csv.reader(file)
    data = [row for row in reader]

## count the sums for every ten years
    count = 0
    sums= []
    sum_decade= 0
    for i in range(1, len(data)):
        for g in range(1,13):
            count+=1
            sum_decade += float(data[i][g])
            g+=1
            if count == 120:
                sums.append(sum_decade)
                sum_decade= 0
                count=0
        i+=1

## Get the average of each decades, and format it nicely with .1f
average =[]
for i in range(len(sums)):
    average.append(format(sums[i]/120, '.2f'))

print(average)

