import csv

"""This python-file will split a big csv-file into a smaller one according to the date"""
header = []
data = []

with open('wiwosearch_all.csv', 'r') as readdata:
   reader = csv.reader(readdata, delimiter=',')
   header = next(reader)

   for row in reader:
       # specify the criterion
       if "Dezember 2021" in row[2]:
           print(row[2]+" "+row[0])
           data.extend([row])

#specify the name of the new file
with open('ww_dec21.csv', 'w') as result:
   writer = csv.writer(result, delimiter=',')
   writer.writerow(header)
   writer.writerows(data)