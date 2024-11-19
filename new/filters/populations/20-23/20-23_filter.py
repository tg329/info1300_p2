import pandas as pd

# define file path
file_path = 'pre-20-23.csv'

#read file, but also drop unnecessary rows that are not 50 states, dc, pr
year20to23 = pd.read_csv(file_path, delimiter=',', skiprows= 
                         [0,1,2,3,4,5,6,7,60,62,63,64,65,66,67,68])

#rename lines with things necessary we want to keep
year20to23.columns = ["States", "Estimate1", "2020", "2021", "2022", "2023"]

#drop unnecessary rows
year20to23.drop('Estimate1', axis=1, inplace=True)

#remove '.' before states
year20to23['States'] = year20to23['States'].str.lstrip('.')

year20to23.to_csv('20-23.csv', index=False)
