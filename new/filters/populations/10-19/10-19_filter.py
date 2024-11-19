import pandas as pd

# define file path
file_path = 'pre-10-19.csv'

#read file, but also drop unnecessary rows that are not 50 states, dc, pr
year10to19 = pd.read_csv(file_path, delimiter=',', skiprows= 
                         [0,1,2,3,4,5,6,7,60,62,63,64,65,66,67,68])

#rename lines with things necessary we want to keep
year10to19.columns = ["States", "Estimates1","Estimates2", "2010", "2011", "2012", "2013", 
                      "2014", "2015","2016", "2017", "2018", "2019", "Estimate3", "Estimates4"]

#drop unnecessary rows
year10to19.drop('Estimates1', axis=1, inplace=True)
year10to19.drop('Estimates2', axis=1, inplace=True)
year10to19.drop('Estimate3', axis=1, inplace=True)
year10to19.drop('Estimates4', axis=1, inplace=True)

#remove '.' before states
year10to19['States'] = year10to19['States'].str.lstrip('.')

year10to19.to_csv('10-19.csv', index=False)
