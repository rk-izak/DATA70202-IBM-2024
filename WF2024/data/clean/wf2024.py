import os
import pandas as pd

dirs = {
    "../raw/working-futures-2024/regions": "./working-futures-2024/regions",
    "../raw/working-futures-2024/subregions": "./working-futures-2024/subregions"
}

# List of sheet names to extract
"""
Computer, etc [26] - 16
Telecommunications [61] - 44
Computing services [62] - 45
Information services [63] - 46
Scientific research and development [72] - 54
Financial services [64] - 47
Education [85] - 65
Health [86] - 66
"""

sheets_to_extract = ['Ind75-16', 'Ind75-44', 'Ind75-45', 'Ind75-46', 
                     'Ind75-54', 'Ind75-47', 'Ind75-65', 'Ind75-66']

# Loop through all directories and files
for dir, output_directory in dirs.items():
    if not os.path.exists(output_directory):
        os.makedirs(output_directory, exist_ok=True)  # Ensure the output directory exists

    for filename in os.listdir(dir):
        if filename.endswith('.xlsm'):
            # Construct the full file path
            file_path = os.path.join(dir, filename)

            # Load the workbook
            with pd.ExcelFile(file_path, engine='openpyxl') as xls:
                # Check each sheet in the workbook
                for sheet_name in xls.sheet_names:
                    if sheet_name in sheets_to_extract:
                        # Read the specific sheet
                        df = pd.read_excel(xls, sheet_name=sheet_name)

                        # Save the sheet to a new CSV file
                        new_filename = f"{os.path.splitext(filename)[0]}_{sheet_name}.csv"
                        df.to_csv(os.path.join(output_directory, new_filename), index=False)

print("Sheets extraction complete.")
