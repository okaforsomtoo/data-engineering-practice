"""
Beginner data-engineering practice project using pandas.

The script demonstrates a simple batch pipeline: read a CSV, clean missing
numeric values, add a derived high-earner flag, filter matching rows, and
write the result to a new CSV file.
"""
import pandas as pd

def read_data(filename):
    """Load a CSV file into a DataFrame and report how many rows it contains."""
    try:
        df = pd.read_csv(filename)
        print(f"Data loaded successfully - {len(df)} rows found")
        return df
    except FileNotFoundError:
        print("File not found. Check the filename.")
        return None

# First, practice loading and inspecting the source data.
df = read_data ("people.csv")
print(df)

def clean_data(df):
    """Fill missing age and salary values with their respective column means."""
    # Mean imputation keeps incomplete records in the dataset for later steps.
    df["age"] = df["age"].fillna(df["age"].mean())
    df["salary"] = df["salary"].fillna(df["salary"].mean())
    print(f"Data cleaned successfully")
    return df

# Practice the cleaning step independently before adding transformations.
df = read_data("people.csv")
df = clean_data(df)
print(df)

def transform_data(df):
    """Add a Boolean flag for rows with a salary strictly above £50,000."""
    # Comparing each salary to the threshold produces True/False values.
    df["high_earner"] = df["salary"] > 50000
    print("Data transformed succesfully")
    return df

# Inspect the derived flag before using it to select rows.
df = read_data("people.csv")
df = clean_data(df)
df = transform_data(df)
print(df)

def filter_data(df):
    """Return only rows whose high_earner flag is True."""
    # A Boolean mask selects matching rows while retaining all their columns.
    high_earners = df[df["high_earner"] == True]
    print(f"Filter complete - {len(high_earners)} high earners found")
    return high_earners

# Practice extracting the selected employees as a separate result.
df = read_data("people.csv")
df = clean_data(df)
df = transform_data(df)
high_earners = filter_data(df)
print(high_earners)

def write_data(df, filename):
    """Save a DataFrame as a CSV file without writing its row index."""
    try:
        # The index is a pandas row label, not a source-data column.
        df.to_csv(filename, index=False)
        print(f"Data written succesfuflly to {filename}")
    except Exception as e:
        print(f"Error writing file - {e}")

# Final end-to-end run: reload the source, apply each stage, and export results.
df = read_data("people.csv")
df = clean_data(df)
df = transform_data(df)
high_earners = filter_data(df)
write_data(high_earners, "high_earners.csv")