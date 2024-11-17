import pandas as pd

def function1(df):
    """
    Define a function to handle missing values in the input pandas dataframe.

    Args:
        df (pandas.DataFrame): The input pandas dataframe with missing values.

    Returns:
        pandas.DataFrame: The input pandas dataframe with missing values replaced.
    """

    # Replace missing values with mean of each column
    df.fillna(df.mean(), inplace=True)

    return df

def function2(df):
    """
    Define a function to drop duplicate rows from the input pandas dataframe.

    Args:
        df (pandas.DataFrame): The input pandas dataframe.

    Returns:
        pandas.DataFrame: The input pandas dataframe with duplicate rows dropped.
    """

    # Drop duplicate rows
    df.drop_duplicates(inplace=True)

    return df

def function3(df, columns_to_keep=None, data_types=None):
    """
    Define a function to filter out specific columns based on user-defined criteria.

    Args:
        df (pandas.DataFrame): The input pandas dataframe.
        columns_to_keep (list or None): A list of column names to keep. If None, all columns are kept.
        data_types (dict or None): A dictionary where keys are column names and values are the desired data types. If None, all columns are kept.

    Returns:
        pandas.DataFrame: The filtered input pandas dataframe.
    """

    # Check if columns_to_keep or data_types is provided
    if columns_to_keep is not None:
        df = df[columns_to_keep]
    elif data_types is not None:
        for column, dtype in data_types.items():
            df[column] = pd.to_datetime(df[column], dtype=dtype)

    return df

def function4(df):
    """
    Define a function to handle categorical variables in the input pandas dataframe.

    Args:
        df (pandas.DataFrame): The input pandas dataframe with categorical variables.

    Returns:
        pandas.DataFrame: The input pandas dataframe with categorical variables handled.
    """

    # Handle one-hot encoding for categorical variables
    categorical_cols = df.select_dtypes(include=['object']).columns
    for col in categorical_cols:
        df = pd.get_dummies(df, columns=[col])

    return df

def function5(df):
    """
    Define a function to handle numerical columns with missing values or outliers.

    Args:
        df (pandas.DataFrame): The input pandas dataframe with numerical columns.

    Returns:
        pandas.DataFrame: The input pandas dataframe with numerical columns handled.
    """

    # Identify columns that are numerical
    numeric_cols = df.select_dtypes(include=[int, float]).columns

    for col in numeric_cols:
        # Replace missing values with mean or median
        if df[col].isna().sum() > 0:
            if df[col].dtype == 'float64':
                df[col].fillna(df[col].median(), inplace=True)
            else:
                df[col].fillna(df[col].mean(), inplace=True)

        # Handle outliers using Z-score method
        z_scores = (df[col] - df[col].mean()) / df[col].std()
        threshold = 3.0
        outlier_indices = [index for index, score in enumerate(z_scores) if abs(score) > threshold]
        df.drop(outlier_indices, inplace=True)

    return df

# Combine the functions into one
def data_processing(df):
    function1(df)
    function2(df)
    function3(df)
    function4(df)
    function5(df)
    return df