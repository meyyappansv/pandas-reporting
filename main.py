import pandas as pd
import xlsxwriter

# Read CSV file into pandas DataFrame
df = pd.read_csv('test_formatted.csv')



# Create a new Excel workbook and add a worksheet
workbook = xlsxwriter.Workbook('test.xlsx')
worksheet = workbook.add_worksheet()

# Define colors
red_format = workbook.add_format({'bg_color': '#FFC7CE', 'font_color': '#9C0006'})
green_format = workbook.add_format({'bg_color': '#C6EFCE', 'font_color': '#006100'})
blue_format = workbook.add_format({'bg_color': '#9FC5E8', 'font_color': '#000080'})

# Write data from DataFrame to Excel worksheet
for i, col in enumerate(df.columns):
    worksheet.write(0, i, col)
for r in range(len(df)):
    for c in range(len(df.columns)):
        header = df.columns[c]
        value = df.iloc[r, c]
        #print(f"HEADER: {header}")
        print(f"VALUE: {value}")
        if "RESULT" in header and value == "FAIL":
            worksheet.write(r + 1, c, value,red_format)
        elif "RESULT" in header and value == "PASS":
            worksheet.write(r + 1, c, value, green_format)
        elif value == "N/A":
            worksheet.write_string(r + 1, c, "NA")
        else:
            worksheet.write_string(r + 1, c, str(value))
# # Close the workbook
workbook.close()
