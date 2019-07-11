import folium
import pandas

map = folium.Map(location=[40, -100], zoom_start=6)

#for coordinates in [[40.5, -100.5],[39.5, -99.5]]:
#    fg.add_child(folium.Marker(location=coordinates, popup="Hi!", icon=folium.Icon(color="green")))
#
#map.add_child(fg)
#map.save("mapping.html")

df = pandas.read_csv("./Volcanoes.txt")

name = list(df["NAME"])
elev = list(df["ELEV"])
lat = list(df["LAT"])
lon = list(df["LON"])

def color_producer(elev):
    if(elev < 1000):
        return "green"
    
    elif(1000 < elev < 3000):
        return "orange"
    
    else:
        return "red"

fgv = folium.FeatureGroup(name="Volcanoes")
for nm, el, lt, ln in zip(name, elev, lat, lon):
    info = nm + ", " + str(el) + "m"
    fgv.add_child(folium.Marker(location=[lt,ln], popup=folium.Popup(info, parse_html=True), icon=folium.Icon(color=color_producer(el), icon="glyphicon glyphicon-scissors")))


def map_color(value):
    if value > 10000000:
        return {"fillColor":"red"}
    else:
        return {"fillColor":"green"}

fgp = folium.FeatureGroup(name="Population")
fgp.add_child(folium.GeoJson(data = open("world.json", "r", encoding='utf-8-sig').read(), style_function = lambda x: map_color(x["properties"]["POP2005"])))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("mapping.html")
