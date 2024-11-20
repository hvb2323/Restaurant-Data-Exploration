#level1 task3 ::: Geospatial analysis

#we need to analyze the geospatial like latitude and longitude and further we wanted to map them on map
#we can use folium package fro mapping
#lets start


#lets import some libraries for the mapping the cluster based on the location


#let us find the correlation among the restaurants and locations./latitude and rating
#lets perform fro latitude and rating
import pandas as pd
import folium
from folium.plugins import MarkerCluster 
from scipy.stats import pearsonr

#lets read the data

df=pd.read_csv('Dataset.csv')



#Succefully loaded

#let perform the mapping\

mapping=folium.Map(location= [df['Latitude'].mean(),df['Longitude'].mean()],zoom_start=2)

#lets create some markibng As cluster in relating nearer places

mc=MarkerCluster().add_to(mapping)

for i,row in df.iterrows():
    folium.Marker([row['Latitude'],row['Longitude']],popup=row['Restaurant Name']).add_to(mc)

mapping.save('restaurant.html')


correlation,p_value=pearsonr(df["Latitude"],df['Aggregate rating'])
print(f"Correlaion: {correlation}")
print(f"p-value: {p_value}")