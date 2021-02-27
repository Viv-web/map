import folium

map = folium.Map(location=[55.753215, 37.622504], zoom_start = 8)

map.add_child(folium.LatLngPopup())

map.save("map.html")
