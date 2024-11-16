import pandas as pd

file_path = 'pre-20-23.csv'
year20to23 = pd.read_csv(file_path, delimiter=',', skiprows= 
                         [0,1,2,3,4,5,6,7,8,60,62,63,64,65,66,67,68])

year20to23.columns = ["States", "Base", "2020", "2021", "2022", "2023"]
year20to23.drop('Base', axis=1, inplace=True)
year20to23['States'] = year20to23['States'].str.lstrip('.')

year20to23.to_csv('20-23.csv', index=False)