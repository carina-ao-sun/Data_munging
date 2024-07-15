f = open(r"data\nasa_data.txt" , "r")
content2= []
content = f.readlines()
content1 = content[7:-6]
content2.append(content1[0])
for i in range(0,len(content1)):
    content1[i]=content1[i].strip()
content1 = [ i for i in content1 if i]
for i in range(0,len(content1)):
    if "Jan" not in content1[i] or content1[i] == '':
        content2.append(content1[i])


# content2 is the sheet in proper format
# If data is NAN, it will be 0+
for i in range(len(content2)):
    content2[i] = content2[i].replace("*", "0")

#covert to list, then calculate the elements in the list
number_list=[]
for i in range(1,len(content2)):
    number_list.append(list(map(int,content2[i].split())))
    i+=1
content2[0]=list(map(str,content2[0].split()))

#convert to F
for i in range(len(number_list)):
    for g in range(1,len(number_list[i])-1):
        number_list[i][g]= format(number_list[i][g]*0.018, '.1f')
        g+=1
    i+=1


for i in range(1,len(content2)):
    content2[i]= number_list[i-1]
    i+=1

# export to csv
import csv

with open('clean_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(content2)
