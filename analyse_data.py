import pandas as pd
import glob

file_list = glob.glob('/Users/juliakarst/PycharmProjects/NewsWebcrawler/wiwo/*.csv')

def analyse(input_files):
      for file in input_files:
            results = pd.read_csv(file)
            print(file)
            print("Lines: ", len(results))
#results = pd.read_csv('/Users/juliakarst/PycharmProjects/NewsWebcrawler/csv_data_and_scripts/big_csv_files/tagesspiegelall.csv')

analyse(file_list)
