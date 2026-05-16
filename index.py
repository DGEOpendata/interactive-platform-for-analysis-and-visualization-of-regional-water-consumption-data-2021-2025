python
import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
import seaborn as sns
from matplotlib import pyplot as plt

# Step 1: Load the CSV data
file_path = 'water_consumption_2021_2025.csv' # Replace with your actual path
data = pd.read_csv(file_path)

# Step 2: Preprocess the data
data['Year'] = pd.to_datetime(data['Year'], format='%Y')
data_grouped = data.groupby(['Region', 'Year']).sum().reset_index()

# Step 3: Plotting water consumption trends
def plot_water_consumption(data):
    plt.figure(figsize=(14, 8))
    sns.lineplot(x='Year', y='Water Consumption (Million m3)', hue='Region', data=data)
    plt.title('Water Consumption Trends by Region (2021-2025)')
    plt.xlabel('Year')
    plt.ylabel('Water Consumption (Million m3)')
    plt.legend(title='Region')
    plt.grid(True)
    plt.show()

plot_water_consumption(data_grouped)

# Step 4: Generate a Geographical Heatmap
# Load shapefile or GeoJSON of the regions
shapefile_path = 'regions_shapefile.geojson' # Replace with your actual shapefile path
geo_data = gpd.read_file(shapefile_path)

# Merge data with geographic data
geo_data = geo_data.merge(data[data['Year'] == '2025'], left_on='Region_Name', right_on='Region')

# Plot the heatmap
fig, ax = plt.subplots(1, 1, figsize=(15, 10))
geo_data.plot(column='Water Consumption (Million m3)', ax=ax, legend=True, 
              cmap='YlGnBu', legend_kwds={'label': "Water Consumption (Million m3)"})
plt.title('Water Consumption Heatmap (2025)')
plt.show()

# Step 5: Save the processed data for users to download
output_path = 'processed_water_data.csv'
data_grouped.to_csv(output_path, index=False)
print(f"Processed data saved to {output_path}")
