# Import the map-making tool
import folium

# Create a map centered on Vietnam
my_map = folium.Map(location=[21.0285, 105.8542], zoom_start=8)

# RED = Crowded
folium.Marker(
    location=[20.9501, 107.0866],
    popup="Ha Long Bay - CROWDED (tourist hotspot)",
    icon=folium.Icon(color='red', icon='warning-sign')
).add_to(my_map)

# GREEN = Peaceful, not crowded
folium.Marker(
    location=[23.278194, 105.363136],
    popup="Ha Giang Loop - PEACEFUL (offbeat gem) ✨",
    icon=folium.Icon(color='green', icon='leaf')
).add_to(my_map)

# ORANGE = Bustling but not crowded
folium.Marker(
    location=[21.0355, 105.8495],
    popup="84 Hang Bac Street, Hanoi - BUSTLING (moderate)",
    icon=folium.Icon(color='orange', icon='info-sign')
).add_to(my_map)

# Save the map
my_map.save('vietnam_travel_map.html')

print("✅ Vietnam travel map created!")
print("🔴 Red = Crowded tourist spots")
print("🟢 Green = Peaceful hidden gems")
print("🟠 Orange = Bustling but manageable")
