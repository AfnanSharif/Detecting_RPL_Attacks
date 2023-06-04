import pandas as pd
import glob

# Path to the directory containing the CSV files
directory_path = "Results/"

# Get a list of all CSV files in the directory
csv_files = glob.glob(directory_path + "*.csv")

# Create an empty DataFrame to store the combined data
combined_data = pd.DataFrame()

# Iterate over each CSV file and append its contents to the combined DataFrame
for file in csv_files:
    df = pd.read_csv(file)
    combined_data = combined_data._append(df, ignore_index=True)

# Save the combined data to a new CSV file
combined_data.to_csv("combined_data.csv", index=False)
