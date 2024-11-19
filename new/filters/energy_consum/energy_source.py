import pandas as pd

# define file paths for the input CSV files
file_path = 'organised_Gen.csv'
state_path = 'states.csv'

# make the dataframe
energy_df = pd.read_csv(file_path, delimiter=',')
states_df = pd.read_csv(state_path, delimiter=',')
energy_df = energy_df[energy_df['ENERGY SOURCE'] != 'Total']

# group the energy data by state, year, and energy source
# summing up generation values.
aggregated_data = energy_df.groupby(
    ['STATE', 'YEAR', 'ENERGY SOURCE']
)['GENERATION (Megawatthours)'].sum().reset_index()

#prepare for merge. merge left join on state
states_df = states_df.rename(columns={'Code': 'STATE'})
yearly_df = states_df.merge(aggregated_data, on = 'STATE', how = 'left')

#drop unnecessary columns
yearly_df.drop('Abbrev', axis=1, inplace=True)
yearly_df.drop('STATE', axis=1, inplace=True)

yearly_df.to_csv('source_years.csv', index=False)
