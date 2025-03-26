#CHARGE_RATE for top 3

import pandas as pd

# Load the Excel file
file_path = "cph.xlsx"  # Replace with your actual file path
df = pd.read_excel(file_path)

# Get the top 3 most duplicated WORKPLACE_IDs
top_3_workplaces = df['WORKPLACE_ID'].value_counts().nlargest(3).index

# Analyze charge rates for each of the top 3 workplaces
for workplace in top_3_workplaces:
    filtered_df = df[df['WORKPLACE_ID'] == workplace]
    
    most_common_charge_rate = filtered_df['CHARGE_RATE'].mode()[0]  # Most frequent
    max_charge_rate = filtered_df['CHARGE_RATE'].max()  # Maximum
    min_charge_rate = filtered_df['CHARGE_RATE'].min()  # Minimum
    
    # Print results
    print(f"\nWORKPLACE_ID: {workplace}")
    print(f"Most common CHARGE_RATE: {most_common_charge_rate}")
    print(f"Maximum CHARGE_RATE: {max_charge_rate}")
    print(f"Minimum CHARGE_RATE: {min_charge_rate}")
