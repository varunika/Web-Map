import folium
import pandas

data = pandas.read_csv("simplemaps-worldcities-basic.csv")
latitude = list(data["lat"])
longitude = list(data["lng"])
population = list(data["pop"])
map = folium.Map(location=[28.579795, 77.222459],zoom_start=6, tiles="Mapbox Control Room")

fg1 = folium.FeatureGroup(name="Markers")
fg2 = folium.FeatureGroup(name="Population shades")

def decide_color(p1):
    if (p1<=200000):
        return "green"
    elif (200000< p1 <600000):
        return "orange"
    else :
        return "red"


for lt, ln, pop in zip(latitude,longitude,population):
    fg1.add_child(folium.CircleMarker(location=[lt,ln], radius=6, fill=1, fill_opacity=0.7, popup=str(pop), color="grey", fill_color=decide_color(pop)))

fg2.add_child(folium.GeoJson(data =open("world.json", 'r', encoding = "utf-8-sig").read(), style_function= lambda x : {'fillColor':"green" if x['properties']['POP2005']<3000000 else 'orange' if 3000000< x['properties']['POP2005']<60000000 else 'red'}))

map.add_child(fg1)
map.add_child(fg2)
map.add_child(folium.LayerControl())

map.save("Map.html")
