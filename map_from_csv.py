import folium
import csv

# Create map centered on Vietnam
my_map = folium.Map(location=[16.0, 108.0], zoom_start=6)

# Read the CSV file we just created
with open('osm_vietnam_places.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    
    for row in reader:
        name = row['name']
        lat = float(row['latitude'])
        lon = float(row['longitude'])
        place_type = row['type']
        
        # Different colors for different types
        if place_type == 'attraction':
            color = 'red'
        elif place_type == 'viewpoint':
            color = 'green'
        elif place_type == 'beach':
            color = 'blue'
        else:
            color = 'gray'
        
        # Add marker
        folium.Marker(
            location=[lat, lon],
            popup=f"<b>{name}</b><br>Type: {place_type}",
            icon=folium.Icon(color=color)
        ).add_to(my_map)

# Save map
my_map.save('osm_map.html')
print(f"Map created with real OSM data!")
print("Open osm_map.html to see it")