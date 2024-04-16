import pandas as pd
from csv_schema import dtype_dict

csv_schema = {
    'COL1': int,
    'RESULT': str,
    'COL2': int,
    'ENO1[1-2]': int,
}
df = pd.read_csv('./test_formatted.csv',dtype=dtype_dict)
print(df.info())