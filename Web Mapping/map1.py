import folium
import pandas

map = folium.Map(location = [43.663688, -79.391519], zoom_start = 7, title = "Stamen Terrain")
data = pandas.read_csv("Volcanoes.txt")
lon = list(data["LON"])
lat = list(data["LAT"])
elev = list(data["ELEV"])


fg = folium.FeatureGroup(name = "My map")
for la, lo, el in zip(lat, lon, elev):
    fg.add_child(folium.Marker(location = [la, lo], popup= "Elevation: \n" + str(el) + " meters", icon= folium.Icon(color="red")))

map.add_child(fg)
map.save("Map1.html")