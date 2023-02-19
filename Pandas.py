#Pandas
import pandas as pd
d= {
    'name':['A', 'B', 'C', 'D'],
    'marks': [12, 34, 23, 53]
    }
df= pd.DataFrame(d)
print(df)
#df.to_csv('details.csv')       #convert to CSV file
df= pd.read_csv('details.csv')
print(df)
