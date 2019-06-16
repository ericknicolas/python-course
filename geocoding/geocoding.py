from geopy.geocoders import ArcGIS
import pandas

#some tests

geolocator = ArcGIS()
location = geolocator.geocode("francesc eiximenis, Sabadell")
#print(location.raw)

location_reverse = geolocator.reverse("42.59944444, -5.56666667")
#print(location_reverse.address)

#code
df = pandas.read_csv("./supermarkets.csv")
df["Address"] = df["Address"] + ", " + df["City"] + ", " + df["State"] + ", " + df["Country"]

df["Coordinates"] = df["Address"].apply(geolocator.geocode)
#print(df)

df["Latitude"] = df["Coordinates"].apply(lambda x: x.latitude)
df["Longitude"] = df["Coordinates"].apply(lambda x: x.longitude)
print(df)