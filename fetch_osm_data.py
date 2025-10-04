import overpy
import csv

# Connect to OpenStreetMap
api = overpy.Overpass()

# Query for tourist attractions in Vietnam
query = """
[out:json];
area["ISO3166-1"="VN"][admin_level=2];
(
  node["tourism"="attraction"](area);
  node["tourism"="viewpoint"](area);
  node["natural"="beach"](area);
);
out body 20;
"""

print("Fetching data from OpenStreetMap...")
result = api.query(query)

# Save to CSV
with open('osm_vietnam_places.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['name', 'latitude', 'longitude', 'type'])
    
    for node in result.nodes:
        name = node.tags.get("name", "Unnamed")
        lat = node.lat
        lon = node.lon
        place_type = node.tags.get("tourism", node.tags.get("natural", "unknown"))
        
        writer.writerow([name, lat, lon, place_type])
        print(f"Added: {name} ({lat}, {lon})")

print(f"\nFound {len(result.nodes)} places!")
print("Data saved to osm_vietnam_places.csv")