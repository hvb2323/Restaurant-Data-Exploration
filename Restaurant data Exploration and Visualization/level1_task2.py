#task 2 DESCRIPTIVE ANALYSIS'
#1 CALCULATING BASIC STATISTICAL MEASURES(MEAN,MEDIAN,STANDARD DEVIATION) FOR NUMERICAL COLUMNS
#HENCE LET RETRIEVE THE NUMERICAL COLUMNS
#BEFORE GOING INTO PROCESS IMPORT SOME LIBRARIES 
#We are going to import pandas for dealing with the'dataset.csv'
import pandas as pd
import matplotlib.pyplot as plt
#lets load the data

df=pd.read_csv('Dataset.csv')


# the numerical columns contains numeric data which are nnumbers so let retrieve those using select_dtypes including
#number

Num_data=df.select_dtypes(include=['number'])

#lets check whether retrieved or not

print("NUmerical columns \n",Num_data)

#lets now retrieve the data other than number that may be strings
#for this we are including objects

Cate=df.select_dtypes(include=['object'])

#lets check 

print("\nCategorical data\n",Cate)

#lets move fyrther into our descriptive analysis lets visualize the distributions among the categorical variables,
#such as "Country code","city","Cuisines"
#before that we need to import visualizing library such as matplotlib
#lets go
Count_of_Country_code=df["Country Code"].value_counts()
print("\n COuntry code Distribution\n",Count_of_Country_code)


#here we using the count for count the total countries among the data visualiing on country pattern
plt.figure(figsize=(12,6))
Count_of_Country_code.plot(kind='bar')
plt.title("distribution of country code" )
plt.xlabel("Country code")
plt.ylabel("frequent")
plt.show()

#lets for the city

Count_of_cities=df['City'].value_counts()
print("\n City distribution\n",Count_of_cities)

#lets plot

plt.figure(figsize=(10,6))
Count_of_cities.plot(kind='bar')
plt.title("cities distribution")
plt.xlabel("cities")
plt.ylabel("frequent")
plt.show()

#lets for cuisine 
Count_cuisine=df['Cuisines'].value_counts()
print("\n Cuisines Distribution\n",Count_cuisine.head(10))
#we cannot retreive uniqueness distribution plotting hence we are not visualizing
#now for no of restaurants at top let retrieve top 10

Top_restaurant=df['Restaurant Name'].value_counts()
print("\n top restaurants\n",Top_restaurant)



#
