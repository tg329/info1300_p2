import pandas as pd

file_path = 'pre-00-09.csv'
year10to19 = pd.read_csv(file_path, delimiter=',', skiprows= 
                         [0,1,2,3,4,5,6,7,8,60,62,63,64,65,66,67,68,69])



year10to19.columns = ["States", "Estimate1", "2000", "2001", 
                      "2002", "2003", "2004","2005", "2006", "2007", "2008", 
                      "2009", "Estimate2", "Estimate3"]
year10to19.to_csv('00-09.csv', index=False)

year10to19.drop('Estimate1', axis=1, inplace=True)
year10to19.drop('Estimate2', axis=1, inplace=True)
year10to19.drop('Estimate3', axis=1, inplace=True)
year10to19['States'] = year10to19['States'].str.lstrip('.')

year10to19.to_csv('00-09.csv', index=False)
