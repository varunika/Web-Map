import folium
import pandas

data = pandas.read_csv("Volcanoes_USA.txt")
latitude = list(data["LAT"])
longitude = list(data["LON"])
elevation = list(data["ELEV"])
map = folium.Map(location=[28.579795, 77.222459],zoom_start=6, tiles="Mapbox Bright")

fg1 = folium.FeatureGroup(name="volcanoes")
fg2 = folium.FeatureGroup(name="Population shades")

def decide_color(p1):
    if (p1<=1500):
        return "green"
    elif (1500< p1 <3000):
        return "orange"
    else :
        return "red"


for lt, ln, ele in zip(latitude,longitude,elevation):
    fg1.add_child(folium.CircleMarker(location=[lt,ln], radius=6, fill=1, fill_opacity=0.7, popup=str(ele)+"m", color="grey", fill_color=decide_color(ele)))

fg2.add_child(folium.GeoJson(data =open("world.json", 'r', encoding = "utf-8-sig").read(), style_function= lambda x : {'fillColor':"green" if x['properties']['POP2005']<3000000 else 'orange' if 3000000< x['properties']['POP2005']<60000000 else 'red'}))

map.add_child(fg2)
map.add_child(fg1)
map.add_child(folium.LayerControl())

map.save("Map.html")
