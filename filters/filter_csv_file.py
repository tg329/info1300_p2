import pandas as pd

#file path of the original csv file
file_path = 'filters/original_par_kid_income.csv'
df = pd.read_csv(file_path,delimiter = ',')

#tier is labelled with specifed tier of school. we want 1,2,3,4,5,6
only_top_tier_df = df[df['tier'] <= 6]

#create the number of colleges that we are looking at
numbers = []
for i in range(1,len(only_top_tier_df)+1):
  numbers.append(i)
only_top_tier_df.insert(2, "number", numbers, True)

#columns that we care about
columns = ["number", "name", "tier", "tier_name", "state", "par_median", "k_median", "mr_kq5_pq1"]
select_columns = only_top_tier_df.filter(columns)

#export names of top uni
unis = only_top_tier_df['name']
unis.to_csv('filter/top_unis_name.csv', index=False)

print(type(unis))

#export into csv with the dataframe we manipulated
select_columns.to_csv('top_tier_unis.csv', index=False)