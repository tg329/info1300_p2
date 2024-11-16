import pandas as pd

path_1 = '00-09/00-09.csv'
path_2 = '10-19/10-19.csv'
path_3 = '20-23/20-23.csv'

df1 = pd.read_csv(path_1, delimiter=',', thousands=',')
df2 = pd.read_csv(path_2, delimiter=',', thousands=',')
df3 = pd.read_csv(path_3, delimiter=',', thousands=',')

final_df = df1.merge(df2, on='States', how='outer').merge(df3, on='States', how='outer')
final_df.to_csv('pop_all_years.csv', index=False)