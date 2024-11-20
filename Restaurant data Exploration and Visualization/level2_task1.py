#level2 task1 is to get the following 
# first thing is to get the restaurants with having online booking and tavble booking 
#lets begin

#importing necessary library

import pandas as pd

df=pd.read_csv('Dataset.csv')

#tb->Table booking

total_restaurants_tb=len(df[df['Has Table booking']=='Yes'])

print(f'Totale restaurants with online delivery:\n {total_restaurants_tb}')

#od->ONlinedelivery

total_restaurants_od=len(df[df['Has Online delivery']=='Yes'])

print(f'Totale restaurants with online delivery:\n {total_restaurants_od}')


#lets calculate total restaurants

total=len(df['Restaurant Name'])

print(f'Total Restaurants:\n {total}')


#Lets find the percentage of the both with table booking an online delivery 

total_tb_od=total_restaurants_tb+total_restaurants_od

percentage=((total_tb_od/total)*100)

print(f'Percentage of total restaurants with tb and od :\n {percentage}')

#lets move furrther 

# we are dealing with restaurants average rating with or without the table booking

with_tb_rate=df[df['Has Table booking']=='Yes']['Aggregate rating'].mean()

print(f'Average rating with taable booking:\n {with_tb_rate}')

#now for without the table booking

without_tb_rate=df[df['Has Table booking']=='No']['Aggregate rating'].mean()

print(f'Average rating without table booking:\n{without_tb_rate}')


#lets create the code for retrieving the availability of restaurants based upon the od
#lets treat price range as pr

pr=df['Price range'].unique()
print(pr)
drr={}
#lets create an empty dictionar for the sake of adding the list of availableity percentage of the restaurants based upon the
#the price ranges
#rr for the restaurants in range
for price_range in pr:
    rr=df[df['Price range']==price_range]
    count_rr=len(rr[rr['Has Online delivery']=='Yes'])
    trr=len(rr)
    drr[price_range]=(count_rr/trr)*100

for price_range,delivery_percentage in drr.items():
    print(f'{price_range}:{delivery_percentage}')

    