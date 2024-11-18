import pandas as pd

file_path = 'organised_Gen.csv'
state_path = 'states.csv'
energy_df = pd.read_csv(file_path, delimiter=',')
states_df = pd.read_csv(state_path, delimiter=',')
energy_df = energy_df[energy_df['ENERGY SOURCE'] != 'Total']

aggregated_data = energy_df.groupby(
    ['STATE', 'YEAR', 'ENERGY SOURCE']
)['GENERATION (Megawatthours)'].sum().reset_index()

states_df = states_df.rename(columns={'Code': 'STATE'})

yearly_df = states_df.merge(aggregated_data, on = 'STATE', how = 'left')
yearly_df.drop('Abbrev', axis=1, inplace=True)
yearly_df.drop('STATE', axis=1, inplace=True)

yearly_df.to_csv('source_years.csv', index=False)
