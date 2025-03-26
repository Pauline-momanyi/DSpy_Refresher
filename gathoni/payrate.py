#highest and lowest PAY_RATE and CHARGE_RATE Q3

import pandas as pd

# Load the Excel file (update with your actual file path)
file_path = "cph.xlsx"
df = pd.read_excel(file_path)

# Check column names
print(df.columns)

# Replace 'PayRate' with the actual column name from your file
highest_chargerate = df['CHARGE_RATE'].max()
lowest_chargerate = df['CHARGE_RATE'].min()

highest_payrate = df['PAY_RATE'].max()
lowest_payrate = df['PAY_RATE'].min()

print(f"Highest Chargerate: {highest_chargerate}")
print(f"Lowest Chargerate: {lowest_chargerate}")
print(f"Highest Payrate: {highest_payrate}")
print(f"Lowest Payrate: {lowest_payrate}")