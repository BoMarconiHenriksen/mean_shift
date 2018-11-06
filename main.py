""" 
The url to run this program use this url:
https://raw.githubusercontent.com/rmlassesen/dataset/master/p_pladser.csv
"""
import utility.downloader as download
import utility.convert_csv as convert_csv
import library.mean as mean

if __name__ == '__main__':
    global file_name
    data_income_file = download.download_file()

data = convert_csv.convert_csv_to_dataframe(data_income_file)

mean.mean_find(data)
