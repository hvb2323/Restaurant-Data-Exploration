#lets import libraries as we are dealing with large data set let us use pandas
import pandas as pd

#the preliminary step ,which is feeding the data i.e loading the data
#using df (dataframe) and read_csv for loading

df=pd.read_csv('Dataset.csv')
#lets check whther data been loaded or not
print(df)
#succefully loaded

#lets proceed with our task exploration and preprocessing

#checking the no.of rows and columns
#for this lets use df.shape which retrieve tuple representing the dimensions
#0 for the rows
no_of_rows=df.shape[0]
print("\n Number of Rows:\n",no_of_rows)

#similarly for columns which is df.shape[1]

no_of_columns=df.shape[1]
print("\n Number of columns : \n",no_of_columns)

#succefully retrived the rows and columns count

# now move on to analyze and retrieve the columns with null values or NA valued aloing with their sum
#for this we are going to use the df.isnull() which retrieves NA tuple

empty=df.isnull().sum()
#here we use the sum() for retrieving the total missing value in repective to the columns
print("\n missing values: \n",empty )
#succefully retrieved the empty columns count with repect to columns

#now lets get into the imbalances in the aggregate ratings
#here we are going to count the value count in the aggregate rating count
count=df["Aggregate rating"].value_counts()

print("\n class counts imbalnces \n",count)
