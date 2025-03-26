# Facilities that are duplicated and their CHARGE_RATES Q4

import pandas as pd

# Load the Excel file
file_path = "cph.xlsx"  # Replace with your actual file path
df = pd.read_excel(file_path)

# Count occurrences of each WORKPLACE_ID
workplace_counts = df['WORKPLACE_ID'].value_counts()

# Filter for workplace IDs that appear more than once
duplicate_workplaces = workplace_counts[workplace_counts > 1].index

# Create a dictionary to store charge rate stats
charge_rate_stats = []

# Loop through duplicated workplaces to find charge rate details
for workplace in duplicate_workplaces:
    filtered_df = df[df['WORKPLACE_ID'] == workplace]
    
    most_common_charge_rate = filtered_df['CHARGE_RATE'].mode()[0]  # Most frequent
   
    
    charge_rate_stats.append({
        'WORKPLACE_ID': workplace,
        'Occurrences': len(filtered_df),
        'CHARGE_RATE': most_common_charge_rate
    })

# Convert to DataFrame
charge_rate_df = pd.DataFrame(charge_rate_stats)

# Print results
print(charge_rate_df)

# Optionally, save results to a CSV file
charge_rate_df.to_csv("workplace_charge_rates.csv", index=False)
