import folium

map = folium.Map(location=[55.753215, 37.622504], zoom_start = 8)

folium.Marker(location=[55.753215, 37.622504], popup = "Moscow", icon=folium.Icon(color = "gray")).add_to(map)
map.save("map.html")
