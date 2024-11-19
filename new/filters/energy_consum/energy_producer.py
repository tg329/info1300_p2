import pandas as pd

# define file paths for the input CSV files
file_path = 'organised_Gen.csv'
state_path = 'states.csv'

# make the dataframe
energy_df = pd.read_csv(file_path, delimiter=',')
states_df = pd.read_csv(state_path, delimiter=',')

#filter out rows where the energy source is 'Total'.
energy_df = energy_df[energy_df['ENERGY SOURCE'] == 'Total']

aggregated_data = energy_df.groupby(
    ['STATE', 'YEAR', 'TYPE OF PRODUCER', 'MONTH']
)['GENERATION (Megawatthours)'].sum().reset_index()

final_data = aggregated_data.groupby(
    ['STATE', 'YEAR', 'TYPE OF PRODUCER']
)['GENERATION (Megawatthours)'].sum().reset_index()

#prepare for merge. merge left join on state
states_df = states_df.rename(columns={'Code': 'STATE'})
merged_data = states_df.merge(final_data, on='STATE', how='left')

#drop unnecessary columns
merged_data.drop('Abbrev', axis=1, inplace=True)
merged_data.drop('STATE', axis=1, inplace=True)

merged_data.to_csv('producer_years.csv', index=False)
