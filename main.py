from datetime import datetime
from pytz import timezone
from timezonefinder import TimezoneFinder
from sunnyday import Weather
from folium import Marker

#class file
class Geopoint(Marker):
    def __init__(self, latitude, longitude):
        super().__init__(location=[latitude, longitude])
        self.latitude = latitude
        self.longitude = longitude
    
    def get_time(self):
        my_timezone = TimezoneFinder().timezone_at(lat=self.latitude, lng=self.longitude)
        timezoneString = timezone(my_timezone)
        return datetime.now(timezoneString)
    
    def get_weather(self):
        myWeather = Weather(apikey="70c09db1e85adf76cc8561233d2f562b", lat=self.latitude, lon=self.longitude).next_12h_simplified()
        return myWeather
        
        
        