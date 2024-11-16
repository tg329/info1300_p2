import pandas as pd

path_1 = '00-09/00-09.csv'
path_2 = '10-19/10-19.csv'
path_3 = '20-23/20-23.csv'

df1 = pd.read_csv(path_1, delimiter=',')
df2 = pd.read_csv(path_2, delimiter=',')
df3 = pd.read_csv(path_3, delimiter=',')

final_df = pd.concat([df1, df2,df3], ignore_index=True)
final_df.to_csv('final.csv', index=False)

