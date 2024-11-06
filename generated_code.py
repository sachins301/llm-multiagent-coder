import pandas as pd

def read_csv_file(file_path):
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        print("The file was not found. Please check the file path.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def clean_data(df):
    # Handle missing values
    df.fillna('Unknown', inplace=True)

    # Convert data types if necessary
    for column in df.columns:
        if df[column].dtype == 'object' and df[column].isnull().any():
            df[column] = df[column].fillna('')
        elif df[column].dtype == 'int64':
            df[column] = pd.to_numeric(df[column], errors='coerce')
        elif df[column].dtype == 'float64':
            df[column] = pd.to_numeric(df[column], errors='coerce')

    return df

# You can use this function by calling it with a CSV file path as an argument
file_path = "path_to_your_csv_file.csv"
result = read_csv_file(file_path)
if result is not None:
    cleaned_data = clean_data(result)
    print(cleaned_data.head())