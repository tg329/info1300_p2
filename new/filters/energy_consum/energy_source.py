import pandas as pd

file_path = 'organised_Gen.csv'
energy_df = pd.read_csv(file_path, delimiter=',')
energy_df = energy_df[energy_df['ENERGY SOURCE'] != 'Total']

aggregated_data = energy_df.groupby(
    ['YEAR', 'ENERGY SOURCE']
)['GENERATION (Megawatthours)'].sum().reset_index()

new_data = [['YEAR', 'ENERGY SOURCE', 'GENERATION (Megawatthours)']] + aggregated_data.values.tolist()

yearly_df = pd.DataFrame(new_data[1:], columns=new_data[0])

yearly_df.to_csv('source_years.csv', index=False)
