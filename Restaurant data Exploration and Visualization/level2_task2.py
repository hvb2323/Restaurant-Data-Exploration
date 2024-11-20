#task 2 in level 2 is to price range analysis

#first aspect is to retrieve the most common price range among alla the restaurants 
#first we import the required packages

import pandas as pd
from collections import Counter 
df=pd.read_csv('Dataset.csv')

#print(df)
#succesfully retrieved

#lets go with the price ranges(pr) column

pr=df['Price range']

#print(pr)

#now we need to count the price ranges with total restaurants associated

#for this lets use Counter from collection so import Counter

#counting of pr

cpr=Counter(pr)

#print(cpr)

#now we need to identify the most common from the details

#for that we are using most_common fuction

mcpr=cpr.most_common(1)

#print(mcpr)

# we retrieved the most common price range along with ists count

#lets go for the next aspect 

#retrieving the average rating for each price range 
avg_rating={}
for price_range in set(pr):
    r=df[df['Price range']==price_range]['Aggregate rating']
    avg_rating[price_range]=sum(r)/len(r)
print(avg_rating)

#identifying the color given for the highest average ratings 

h=max(avg_rating)

print(h)
#now retrieve the color correspondance

c=df[df['Price range']==h]['Rating color']
print(c)