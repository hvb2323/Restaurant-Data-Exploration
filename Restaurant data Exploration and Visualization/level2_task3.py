#extracting additional features from existing columns such as the length of the rstaurant name or address
#befor going in lets load the data

import pandas as pd 
df=pd.read_csv('Dataset.csv')

#finding the length of the restaurants name along with their lenght in the given dataset
df['name_length']=df['Restaurant Name'].apply(len)
df["address_length"]=df['Address'].apply(len)
print(df['name_length'])
print(df['address_length'])

#creating new features by encoding new variable 
#it can be chaning the yes or no to 0 and 1

#by using map we can

df['table_booking']=df['Has Table booking'].map({'Yes':1,'No':0})

print(df['table_booking'])