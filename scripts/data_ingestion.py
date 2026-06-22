import pandas as pd
import os

data_path = "data/raw"

csv_files = [f for f in os.listdir(data_path) if f.endswith(".csv")]

print(f"\nFound {len(csv_files)} CSV files")

for file in csv_files:

    print("\n" + "=" * 80)
    print(f"Dataset: {file}")

    file_path = os.path.join(data_path, file)

    try:
        df = pd.read_csv(file_path)

        print("\nShape:")
        print(df.shape)

        print("\nData Types:")
        print(df.dtypes)

        print("\nFirst 5 Rows:")
        print(df.head())

        print("\nMissing Values:")
        print(df.isnull().sum())

        print("\nDuplicate Rows:")
        print(df.duplicated().sum())

    except Exception as e:
        print(f"Error reading {file}: {e}")