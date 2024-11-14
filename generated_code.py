import csv
import pandas as pd

def load_csv(filename):
    data = []
    if not filename.startswith('/'):
        filename = 'combined_file.csv'
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            data.append(row)
    return data

def handle_missing_values(data):
    for row in data:
        for i, value in enumerate(row):
            if value == '':
                row[i] = 'missing'
    return data

def convert_data_types(filename):
    data = load_csv(filename)
    data = handle_missing_values(data)

    df = pd.DataFrame(data)
    for column in df.columns:
        if df[column].dtype == 'object':
            try:
                df[column] = df[column].astype(float)
            except ValueError:
                try:
                    df[column] = df[column].astype(str)
                except ValueError:
                    pass

    return data

def remove_duplicates(filename):
    data = load_csv(filename)
    df = pd.DataFrame(data)

    # Check if there are duplicate rows
    if df.duplicated().sum() > 0:
        df.drop_duplicates(inplace=True)

    return df.to_records(index=False)

def save_cleaned_data(filename, cleaned_data):
    with open(f"{filename}_cleaned.csv", 'w', newline='') as f:
        writer = csv.writer(f)
        for row in cleaned_data:
            writer.writerow(row)

def data_transformation():
    convert_data_types('combined_file.csv')
    cleaned_data = remove_duplicates('combined_file.csv')
    save_cleaned_data("combined_file", cleaned_data)

data_transformation()