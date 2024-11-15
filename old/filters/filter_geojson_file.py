import json
import pandas as pd

#open original json file
with open('filters/original_us_unis.geojson', 'r') as file:
  data = json.load(file)

#open top university names
file_path = 'filters/top_unis_name.csv'
df = pd.read_csv(file_path,delimiter = ',')
name_list = df['name'].tolist()

names_list = [name.strip().lower() for name in name_list]

def filter_geojson_by_names(geojson_data, names_list):
  # Filter the geojson data based on the 'name' field
  filtered_features = [
    feature for feature in geojson_data['features']
    if feature['properties']['name'].strip().lower() in names_list
  ]
  return {
    "type": "FeatureCollection",
      "features": filtered_features
  }

# filter  geoson data using the name list
filtered_geojson = filter_geojson_by_names(data, names_list)


# export the filtered data to a new geojson file
with open('n_us_unis.geojson', 'w') as f:
  json.dump(filtered_geojson, f, indent=2)