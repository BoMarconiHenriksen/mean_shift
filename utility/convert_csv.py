import pandas as pd
from tqdm import tqdm


def convert_csv_to_dataframe(data_income_file):
    for row in tqdm(data_income_file, total=len(data_income_file)): 
        data_income = pd.read_csv(data_income_file, sep=',', low_memory=False, usecols=[1, 6, 8])

    """ data_income['FAMILIETYPE'] = pd.to_numeric(
        data_income['FAMILIETYPE'], errors='coerce').fillna(0).astype(int) """
    
    # data_income = data_income[data_income['AAR'] == 2014]
    
    return data_income