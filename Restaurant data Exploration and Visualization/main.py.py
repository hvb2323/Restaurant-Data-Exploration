import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import folium
from folium.plugins import MarkerCluster
from scipy.stats import pearsonr


def load_data(file_path):
    """Load dataset."""
    return pd.read_csv(file_path)


def explore_data(df):
    """Perform exploratory data analysis."""
    print("Dataset Head:\n", df.head())
    print("\nNumber of Rows:", df.shape[0])
    print("Number of Columns:", df.shape[1])
    print("\nMissing Values by Column:\n", df.isnull().sum())
    print("\nClass Count Imbalances in 'Aggregate rating':\n", df["Aggregate rating"].value_counts())


def descriptive_analysis(df):
    """Perform descriptive analysis."""
    numerical_data = df.select_dtypes(include=['number'])
    categorical_data = df.select_dtypes(include=['object'])
    print("\nNumerical Data:\n", numerical_data.head())
    print("\nCategorical Data:\n", categorical_data.head())

    country_code_distribution = df["Country Code"].value_counts()
    city_distribution = df["City"].value_counts()

    # Visualize Country Code Distribution
    plt.figure(figsize=(12, 6))
    country_code_distribution.plot(kind='bar')
    plt.title("Distribution of Country Code")
    plt.xlabel("Country Code")
    plt.ylabel("Frequency")
    plt.show()

    # Visualize City Distribution
    plt.figure(figsize=(10, 6))
    city_distribution.plot(kind='bar')
    plt.title("Cities Distribution")
    plt.xlabel("City")
    plt.ylabel("Frequency")
    plt.show()

    print("\nCuisines Distribution (Top 10):\n", df["Cuisines"].value_counts().head(10))


def geospatial_analysis(df):
    """Perform geospatial analysis and mapping."""
    map_cluster = folium.Map(location=[df['Latitude'].mean(), df['Longitude'].mean()], zoom_start=2)
    mc = MarkerCluster().add_to(map_cluster)

    for _, row in df.iterrows():
        folium.Marker([row['Latitude'], row['Longitude']], popup=row['Restaurant Name']).add_to(mc)

    map_cluster.save('restaurant.html')
    correlation, p_value = pearsonr(df["Latitude"], df["Aggregate rating"])
    print(f"Correlation (Latitude vs Aggregate Rating): {correlation}")
    print(f"P-Value: {p_value}")


def table_online_booking_analysis(df):
    """Analyze restaurants with table and online booking."""
    total_restaurants_tb = len(df[df['Has Table booking'] == 'Yes'])
    total_restaurants_od = len(df[df['Has Online delivery'] == 'Yes'])
    total_restaurants = len(df['Restaurant Name'])

    print(f"Total Restaurants with Table Booking: {total_restaurants_tb}")
    print(f"Total Restaurants with Online Delivery: {total_restaurants_od}")
    print(f"Total Restaurants: {total_restaurants}")

    percentage = ((total_restaurants_tb + total_restaurants_od) / total_restaurants) * 100
    print(f"Percentage with Table Booking or Online Delivery: {percentage:.2f}%")

    avg_rating_with_tb = df[df['Has Table booking'] == 'Yes']['Aggregate rating'].mean()
    avg_rating_without_tb = df[df['Has Table booking'] == 'No']['Aggregate rating'].mean()
    print(f"Average Rating with Table Booking: {avg_rating_with_tb:.2f}")
    print(f"Average Rating without Table Booking: {avg_rating_without_tb:.2f}")


def price_range_analysis(df):
    """Analyze price range and ratings."""
    price_range_counts = Counter(df['Price range'])
    most_common_price_range = price_range_counts.most_common(1)
    print(f"Most Common Price Range: {most_common_price_range}")

    avg_rating = {pr: df[df['Price range'] == pr]['Aggregate rating'].mean() for pr in price_range_counts}
    print("\nAverage Rating by Price Range:\n", avg_rating)


def feature_engineering(df):
    """Create new features from existing columns."""
    df['name_length'] = df['Restaurant Name'].apply(len)
    df['address_length'] = df['Address'].apply(len)
    df['table_booking'] = df['Has Table booking'].map({'Yes': 1, 'No': 0})

    print("\nFeature Engineering - Name Length:\n", df['name_length'])
    print("\nFeature Engineering - Address Length:\n", df['address_length'])
    print("\nFeature Engineering - Table Booking Encoding:\n", df['table_booking'])


def main():
    file_path = 'Dataset.csv'
    df = load_data(file_path)

    print("\n--- Exploration ---")
    explore_data(df)

    print("\n--- Descriptive Analysis ---")
    descriptive_analysis(df)

    print("\n--- Geospatial Analysis ---")
    geospatial_analysis(df)

    print("\n--- Table and Online Booking Analysis ---")
    table_online_booking_analysis(df)

    print("\n--- Price Range Analysis ---")
    price_range_analysis(df)

    print("\n--- Feature Engineering ---")
    feature_engineering(df)


if __name__ == "__main__":
    main()
