#count where IS_VERIFIED is TRUE Q1

import pandas as pd

# Load the Excel file
file_path = "cph.xlsx"
df = pd.read_excel(file_path)

# Convert IS_VERIFIED to boolean (handling string cases)
df['IS_VERIFIED'] = df['IS_VERIFIED'].astype(str).str.upper() == "TRUE"

# Count occurrences where IS_VERIFIED is True
verified_count = df['IS_VERIFIED'].sum()

print(f"Number of verified entries: {verified_count}")
