#where PAY_RATE is higher than CHARGE_RATE FOR VERIFIED shifts Q1

import pandas as pd

# Load the Excel file
file_path = "cph.xlsx"
df = pd.read_excel(file_path)

# Ensure all values in IS_VERIFIED are strings before using .str.upper()
df['IS_VERIFIED'] = df['IS_VERIFIED'].astype(str).str.upper() == "TRUE"

# Filtering based on conditions
filtered_df = df[(df['PAY_RATE'] > df['CHARGE_RATE']) & (df['IS_VERIFIED'] == True)]

# Display the results
print(filtered_df)

# Optionally, save to a new file
filtered_df.to_excel("filtered_results.xlsx", index=False)
