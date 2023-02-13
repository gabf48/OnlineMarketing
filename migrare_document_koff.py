import pandas as pd

df = pd.read_csv('D:\OnlineMarketing\koff.csv', on_bad_lines='skip')

df.to_excel('Final_koff_prod.xlsx', index=False)
