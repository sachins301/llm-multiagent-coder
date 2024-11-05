import pandas as pd
import numpy as np

def read_csv_file(file_path):
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        print("The file was not found.")
        return None

def handle_missing_values(df, method="impute"):
    if method == "impute":
        imputer = pd.DataFrame(np.nanmean(df))
        for column in df.columns:
            if df[column].dtype != 'object':
                df[column] = df[column].fillna(imputer[column])
        return df
    elif method == "remove":
        df.dropna(inplace=True)
        return df
    else:
        print("Invalid method. Please choose either 'impute' or 'remove'.")
        return None

def convert_data_types(df):
    data_types = {"column1": str, "column2": int, "column3": float}
    for column in data_types:
        if column in df.columns:
            df[column] = df[column].astype(data_types[column])
    return df

def remove_duplicates(df):
    try:
        df = df.drop_duplicates()
        return df
    except Exception as e:
        print("An error occurred while removing duplicates:", str(e))
        return None)

def perform_data_cleaning(file_path):
    df = read_csv_file(file_path)
    if df is not None:
        df = handle_missing_values(df)
        df = convert_data_types(df)
        df = remove_duplicates(df)
    return df

# Example usage:
file_path = "path/to/your/file.csv"
cleaned_df = perform_data_cleaning(file_path)
print(cleaned_df)