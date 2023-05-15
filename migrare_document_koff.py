import pandas as pd

df = pd.read_csv('C:\OnlineMarketing\koff_stocks.csv', on_bad_lines='skip')

df.to_excel('Final_koff_prod.xlsx', index=False)
