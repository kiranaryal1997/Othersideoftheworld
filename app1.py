from main import Geopoint
from folium import Map, Popup

#add lat and long if required (other cities or countries)
locations = [[27.71, 85.32],[-33.9, 151.1],[32.25, -110.98]]

#this is not related to locations
my_map = Map(location=[40,2])

# for loc in locations: 
for lat,long in locations: 
    # print(loc)
    #instantiating class
    # geopoint = Geopoint(latitude=loc[0], longitude=loc[1])
    geopoint = Geopoint(latitude=lat, longitude=long)
    #get_weather method to get weather details
    weatherList = geopoint.get_weather()

    #contents popup_inside
    contents = f"""{weatherList[0][0][-8:13]}h {round(weatherList[0][1])}°F <img src="https://openweathermap.org/img/wn/{weatherList[0][3]}@2x.png" width=50>
    <hr>
    {weatherList[1][0][-8:13]}h {round(weatherList[1][1])}°F <img src="https://openweathermap.org/img/wn/{weatherList[1][3]}@2x.png" width=50>
    <hr>
    {weatherList[2][0][-8:13]}h {round(weatherList[2][1])}°F <img src="https://openweathermap.org/img/wn/{weatherList[2][3]}@2x.png" width=50>
    <hr>
    {weatherList[3][0][-8:13]}h {round(weatherList[3][1])}°F <img src="https://openweathermap.org/img/wn/{weatherList[3][3]}@2x.png" width=50>
    <hr>"""

    #Popups
    myPop = Popup(contents, max_width=100)
    myPop.add_to(geopoint)
    geopoint.add_to(my_map)


my_map.save("mymap.html")










