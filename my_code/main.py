import pandas as pd

def extract(file_path):
    """Extract data from a CSV file."""
    return pd.read_csv(file_path)

def transform(df):
    """Transform data (e.g., clean and process)."""
    # Example transformation: remove rows with missing values and add a new column
    df = df.dropna()
    df['processed'] = df['value'] * 2  # Example transformation
    return df

def load(df, output_path):
    """Load transformed data into a new CSV file."""
    df.to_csv(output_path, index=False)

def main():
    # File paths
    input_path = 'data/input.csv'
    output_path = 'data/output.csv'

    # ETL process
    df = extract(input_path)
    df = transform(df)
    load(df, output_path)

if __name__ == "__main__":
    main()
