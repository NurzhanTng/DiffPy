#xlsx->csv
import pandas as pd
xlsx_file = '16.06.xlsx'
df = pd.read_excel(xlsx_file)
csv_file = '16.06.csv'
df.to_csv(csv_file, index=False)


