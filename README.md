# Restaurant Dataset Analysis

This repository contains an exploratory data analysis (EDA) of a restaurant dataset. The analysis includes insights into restaurant ratings, cuisines, pricing, geographical distribution, and various other features. The dataset is primarily focused on restaurant ratings and characteristics across various cities, with additional analyses on features such as online delivery availability and table booking.

## Dataset Overview

The dataset consists of 9,551 rows and 21 columns with the following key attributes:

- **Restaurant ID**: Unique identifier for each restaurant.
- **Restaurant Name**: Name of the restaurant.
- **Country Code**: Country code where the restaurant is located.
- **City**: City where the restaurant is located.
- **Address**: Full address of the restaurant.
- **Locality**: Locality or neighborhood of the restaurant.
- **Longitude** and **Latitude**: Geographical coordinates of the restaurant.
- **Cuisines**: Type(s) of cuisine offered by the restaurant.
- **Average Cost for Two**: Average cost for two people at the restaurant.
- **Currency**: Currency used in the restaurant.
- **Has Table Booking**: Boolean indicating whether the restaurant offers table booking.
- **Has Online Delivery**: Boolean indicating whether the restaurant offers online delivery.
- **Aggregate Rating**: Average rating of the restaurant (from 1 to 5).
- **Votes**: Number of votes received for the restaurant.

## Exploratory Data Analysis (EDA)

### 1. **Missing Values**
The dataset is mostly clean, with only a small number of missing values in the `Cuisines` column.

- **Missing Values**: 9 missing values in `Cuisines`.

### 2. **Class Imbalance in 'Aggregate Rating'**
There is a class imbalance in the `Aggregate Rating` column. Most restaurants have ratings around 4.0, while lower ratings (e.g., `1.8`, `2.0`, etc.) are significantly less common.

### 3. **Numerical Features**
The analysis of numerical features such as `Restaurant ID`, `Longitude`, `Latitude`, `Average Cost for Two`, `Price Range`, `Aggregate Rating`, and `Votes` provide insights into restaurant characteristics and consumer behavior.

### 4. **Cuisines Distribution**
The most common cuisines include:
- **North Indian**
- **North Indian, Chinese**
- **Chinese**
- **Fast Food**

### 5. **Geospatial Analysis**
A very low correlation between latitude and aggregate rating was observed (correlation of 0.0005), suggesting that geographical location does not directly influence restaurant ratings.

### 6. **Table Booking and Online Delivery**
- **Table Booking**: 1,158 restaurants offer table booking.
- **Online Delivery**: 2,451 restaurants offer online delivery.
- **Average Rating**: Restaurants with table booking have an average rating of 3.44, while those without table booking have a lower average rating of 2.56.

### 7. **Price Range Analysis**
- **Most Common Price Range**: Price range 3 (with most restaurants falling within this range).
- **Average Rating by Price Range**:
  - Price Range 1: Rating ~1.99
  - Price Range 2: Rating ~2.94
  - Price Range 3: Rating ~3.68
  - Price Range 4: Rating ~3.82

### 8. **Feature Engineering**
- **Name Length**: Engineered feature based on the length of restaurant names.
- **Address Length**: Engineered feature based on the length of restaurant addresses.
- **Table Booking Encoding**: Binary encoding for whether a restaurant offers table booking.

## Next Steps

### 1. **Data Preprocessing**
- Handle missing data (e.g., imputation of missing `Cuisines` values).
- Address class imbalance in `Aggregate Rating` using techniques such as oversampling or undersampling.

### 2. **Feature Engineering**
- Additional features such as `average_cost_per_person` (derived from `Average Cost for Two`) can be created.
- Further encoding of categorical variables such as `Cuisines`, `City`, or `Restaurant Name` can be performed for machine learning models.

### 3. **Predictive Modeling**
- Build regression or classification models to predict restaurant ratings (`Aggregate Rating`) or categorize them into rating groups (e.g., Excellent, Very Good).
- Evaluate the models using metrics like RMSE, accuracy, and F1-score.

### 4. **Clustering and Segmentation**
- Use clustering techniques such as K-Means to group restaurants based on features like `Price Range`, `Cuisines`, `City`, and `Votes` for marketing or business strategy purposes.

