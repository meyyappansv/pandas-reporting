import pandas as pd
import xlsxwriter
from csv_schema import dtype_dict
import numpy as np


def validate_schema(df):
    try:
        dtype_dict.validate(df)
        print('The DataFrame is valid.')
    except pd.errors.SchemaError as e:
        print(e)
# Read CSV file into pandas DataFrame
df = pd.read_csv('test_formatted.csv',dtype=dtype_dict).set_flags(allows_duplicate_labels=True)
df.replace([np.nan, np.inf, -np.inf], 'NA', inplace=True)
#validate_schema(df)

#Create a new Excel workbook and add a worksheet
workbook = xlsxwriter.Workbook('test_output.xlsx')
worksheet = workbook.add_worksheet()

# Define colors
red_format = workbook.add_format({'bg_color': '#FFC7CE', 'font_color': '#9C0006'})
green_format = workbook.add_format({'bg_color': '#C6EFCE', 'font_color': '#006100'})
blue_format = workbook.add_format({'bg_color': '#9FC5E8', 'font_color': '#000080'})

# Write data from DataFrame to Excel worksheet
# print("COLUMNS")
# print(df.columns)
for i, col in enumerate(df.columns):
    #print(f"I: {i} COL: {col}")
    #Write the header row for the excel spreadsheet
    worksheet.write(0, i, col)
for r in range(len(df)):
    for c in range(len(df.columns)):
        header = df.columns[c]
        value = df.iloc[r, c]
        print(f"HEADER: {header}")
        print(f"VALUE: {value}")
        if "RESULT" in header and value == "FAIL":
            print("Im in FAILED RESULT")
            worksheet.write(r + 1, c, value,red_format)
        elif "RESULT" in header and value == "PASS":
            print("Im in PASS result")
            worksheet.write(r + 1, c, value, green_format)
        elif value == "N/A":
            print("Im in N/A")
            worksheet.write_string(r + 1, c, "NA")
        else:
            print("Im in else clause")
            worksheet.write(r + 1, c, value)
# # Close the workbook
workbook.close()
