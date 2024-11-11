import pandas as pd
import csv

def read_csv_file(file_path):
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        print("File not found. Please check the file path.")
        return None
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None

def handle_missing_values(df):
    # Function to handle missing values in the dataset
    for column in df.columns:
        if df[column].dtype == 'object':
            continue  # skip categorical variables
        mean = df[column].mean()
        median = df[column].median()
        
        # Replace missing values with mean or median
        df[column] = df[column].fillna(mean)
        #df[column] = df[column].fillna(median)
    
    # Remove rows with more than 50% missing values
    threshold = 0.5
    df.dropna(inplace=True, thresh=int(threshold * len(df)))
    return df

def drop_unnecessary_columns(df, min_unique_values=10):
    unnecessary_columns = []
    for column in df.columns:
        if len(df[column].unique()) < min_unique_values or df[column].isna().all():
            unnecessary_columns.append(column)
    
    # Drop the unnecessary columns
    df.drop(columns=unnecessary_columns, inplace=True)
    return df

def perform_data_types_conversion(df):
    numerical_cols = ['column1', 'column2']
    categorical_cols = ['column3', 'column4']

    for col in numerical_cols:
        if col not in df.columns:
            continue
        df[col] = pd.to_numeric(df[col], errors='coerce')

    for col in categorical_cols:
        if col not in df.columns:
            continue
        df[col] = pd.Categorical(df[col]).labels

    return df

def remove_duplicates(df):
    # Function to remove duplicate rows from the dataset based on certain criteria (e.g., identical values across multiple columns)
    unique_df = df.drop_duplicates(subset=['column1', 'column2'], keep='first')
    return unique_df

# Example usage:
file_path = 'path_to_your_csv_file.csv'
df = read_csv_file(file_path)

if df is not None:
    handled_df = handle_missing_values(df)
    print(handled_df.head())  # Print the first few rows of the handled DataFrame
    
    filtered_df = drop_unnecessary_columns(handled_df, min_unique_values=10)
    print(filtered_df.head())

    converted_df = perform_data_types_conversion(filtered_df)
    print(converted_df.head())
    
    unique_df = remove_duplicates(converted_df)
    print(unique_df.head())