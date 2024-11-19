import pandas as pd

file_path = 'organised_Gen.csv'
state_path = 'states.csv'
energy_df = pd.read_csv(file_path, delimiter=',')
states_df = pd.read_csv(state_path, delimiter=',')
energy_df = energy_df[energy_df['ENERGY SOURCE'] != 'Total']

aggregated_data = energy_df.groupby(
    ['STATE', 'YEAR', 'TYPE OF PRODUCER','ENERGY SOURCE', 'MONTH']
)['GENERATION (Megawatthours)'].sum().reset_index()

final_data = aggregated_data.groupby(
    ['STATE', 'YEAR', 'TYPE OF PRODUCER','ENERGY SOURCE']
)['GENERATION (Megawatthours)'].sum().reset_index()

states_df = states_df.rename(columns={'Code': 'STATE'})
merged_data = states_df.merge(final_data, on='STATE', how='left')

merged_data.drop('Abbrev', axis=1, inplace=True)
merged_data.drop('STATE', axis=1, inplace=True)

merged_data.to_csv('new_producer_source_years.csv', index=False)
