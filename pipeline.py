import pandas as pd

def read_data(filename):
    try:
        df = pd.read_csv(filename)
        print(f"Data loaded successfully - {len(df)} rows found")
        return df
    except FileNotFoundError:
        print("File not found. Check the filename.")
        return None
df = read_data ("people.csv")
print(df)

def clean_data(df):
    df["age"] = df["age"].fillna(df["age"].mean())
    df["salary"] = df["salary"].fillna(df["salary"].mean())
    print(f"Data cleaned successfully")
    return df
df = read_data("people.csv")
df = clean_data(df)
print(df)

def transform_data(df):
    df["high_earner"] = df["salary"] > 50000
    print("Data transformed succesfully")
    return df

df = read_data("people.csv")
df = clean_data(df)
df = transform_data(df)
print(df)

#extracting the high earners into a seperate result.

def filter_data(df):
    high_earners = df[df["high_earner"] == True]
    print(f"Filter complete - {len(high_earners)} high earners found")
    return high_earners

df = read_data("people.csv")
df = clean_data(df)
df = transform_data(df)
high_earners = filter_data(df)
print(high_earners)

def write_data(df, filename):
    try:
        df.to_csv(filename, index=False)
        print(f"Data written succesfuflly to {filename}")
    except Exception as e:
        print(f"Error writing file - {e}")

df = read_data("people.csv")
df = clean_data(df)
df = transform_data(df)
high_earners = filter_data(df)
write_data(high_earners, "high_earners.csv")