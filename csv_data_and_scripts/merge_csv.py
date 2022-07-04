import csv
import glob

"This python-file will merge multiple smaller csv-files to one big one"
header = []
data = []

#list of csv-files that will be merged
file_list = glob.glob('/Users/juliakarst/PycharmProjects/NewsWebcrawler/sueddeutsche/*.csv')


def merge_data(input_files):
    for file in input_files:
        with open(file, 'r') as readingfile:
            reader = csv.reader(readingfile, delimiter=',')
            header = next(reader)
            data.extend([row for row in reader])




merge_data(file_list)

with open('sueddeutsche_all.csv', 'w') as result:
    writer = csv.writer(result, delimiter=',')
    writer.writerow(header)
    writer.writerows(data)
