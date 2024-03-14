import pandas as pd


def read_excel_sheet(file_path, sheet_name):
    df = pd.read_excel(file_path, sheet_name=sheet_name, na_values=[''])
    df.fillna('', inplace=True)
    return df
