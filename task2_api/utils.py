from datetime import datetime, timedelta
import numpy as np

from task2_main.models import Measurement, ValidatedMeasurement, InvalidMeasurement

def model_appropriate(old_date_measuremet, latest_date_measurement)-> bool:
    today = datetime.now()
    datetime1=today - timedelta(days=30)
    timedelta1= latest_date_measurement - old_date_measuremet
    if 0 < timedelta1 and datetime1 < latest_date_measurement:
        return True
    else:
        return False

def validate_measurement(sensor, is_error, current_voltage):
    if is_error==False:
        #TODO: if validated create Valideted measurement
        pass
    else:
        #TODO: if invalid create invalid measurement
        pass

#CODE FOR dumb_model FUNCTION HERE
def estimate_coef(x, y):
    # number of observations/points
    n = np.size(x)
 
    # mean of x and y vector
    m_x = np.mean(x)
    m_y = np.mean(y)
 
    # calculating cross-deviation and deviation about x
    SS_xy = np.sum(y*x) - n*m_y*m_x
    SS_xx = np.sum(x*x) - n*m_x*m_x
 
    # calculating regression coefficients
    b_1 = SS_xy / SS_xx
    b_0 = m_y - b_1*m_x
 
    return (b_0, b_1)


# BACKLOG: I want to make a model of voltage_measurement where forecast is also based on the weather in location from IP 
# (like some sensor of voltage in  solar panels) ->two parts
#1)
# # import the module
# import python_weather
# import asyncio

# async def getweather():
#     # declare the client. format defaults to metric system (celcius, km/h, etc.)
#     client = python_weather.Client(format=python_weather.IMPERIAL)

#     # fetch a weather forecast from a city
#     weather = await client.find("Washington DC")

#     # returns the current day's forecast temperature (int)
#     print(weather.current.temperature)

#     # get the weather forecast for a few days
#     for forecast in weather.forecasts:
#         print(str(forecast.date), forecast.sky_text, forecast.temperature)

#     # close the wrapper once done
#     await client.close()

# if __name__ == "__main__":
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(getweather())

#2)MAIN IDEA OF GEOLOCATION 
#!
# from django.http import JsonResponse

# from django.contrib.gis.geoip2 import GeoIP2

# from geopy.geocoders import Nominatim

# from geopy import distance

# import sys



# import models <to do>


# def get_city(ip):
#return city

# def save_user_coordinate(request, latitude, longitude):
#return coordinate

#attach mabe some session_user (?)