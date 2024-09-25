#WeatherApp.py
#Name: Skye Beraz
#Date: 9/22/2024
#Assignment: Homework #1

import WeatherInfo
import datetime

def main():
	WeatherInfo.setKey("446d8459a36091a8012670c35e8f72de")
	weather = "Y"
	time = "morning"
	now = datetime.datetime.now()
	currentHour = now.hour
	if(currentHour >= 0 and currentHour < 12):
		time = "morning"
	elif(currentHour >= 12 and currentHour < 17):
		time = "afternoon"
	else:
		time = "evening"
	while(weather == "Y"):
		WeatherInfo.updateWeather()
		userCity = "Omaha"
		cityDefault = "Omaha"
		print("Good", time + "! Welcome to Skye's Weather App.")
		city = input("Please enter the location you would like a weather-report from. LOCATION: ")
		if(city == ""):
			userCity = cityDefault
		else:
			userCity = city
		WeatherInfo.setCity(userCity)
		WeatherInfo.updateWeather()
		WeatherInfo.getDescription()
		WeatherInfo.getTemp()
		WeatherInfo.getFeelsLike()
		WeatherInfo.getHumidity()
		WeatherInfo.getPressure()
		WeatherInfo.getWindSpeed()
	
		description = WeatherInfo.getDescription()
		temp = WeatherInfo.getTemp()
		feelTemp = WeatherInfo.getFeelsLike()
		humidity = str(WeatherInfo.getHumidity())
		pressure = WeatherInfo.getPressure()
		speed = WeatherInfo.getWindSpeed()
		windDescription = "Calm"
		#temp Kelvin -> Fahrenheit
		tempFloat = 1.8 * (temp - 273.15) + 32
		tempF = round(tempFloat)
		#feels like temp Kelvin -> Fahrenheit
		feelTempFloat = 1.8 * (feelTemp - 273.15) + 32
		feelTempF = round(feelTempFloat)
		#Wind Speed
		MPHFloat = speed * 2.23694
		MPH = round(MPHFloat)
		
		if(MPH < 1):
			windDescription = "calm wind"
		elif(MPH >= 1 and MPH < 4):
			windDescription = "light air"
		elif(MPH >= 4 and MPH < 7):
			windDescription = "light breezes"
		elif(MPH >= 8 and MPH < 12):
			windDescription = "gentle breezes"
		elif(MPH >= 13 and MPH < 18):
			windDescription = "moderate breezes"
		elif(MPH >= 19 and MPH < 24):
			windDescription = "fresh breezes"
		elif(MPH >= 25 and MPH < 31):
			windDescription = "strong breezes"
		elif(MPH >= 32 and MPH < 38):
			windDescription = "high winds"
		elif(MPH >= 39 and MPH < 46):
			windDescription = "gales"
		elif(MPH >= 47 and MPH < 54):
			windDescription = "strong gales"
		elif(MPH >= 55 and MPH < 63):
			windDescription = "stormy winds"
		elif(MPH >= 64 and MPH < 72):
			windDescription = "violent stormy winds"
		elif(MPH >= 73):
			windDescription = "hurricane-level winds"
		else: 
			print("404-WindSpeed Not Found")
		#Jackets
		wear = "You won't need a jacket"
		if(feelTempF < 40):
			wear = "We recommend you wear a heavy coat"
		elif(feelTempF >= 40 and feelTempF < 55):
			wear = "We recommend you wear a medium jacket"
		elif(feelTempF >= 55 and feelTempF < 65):
			wear = "We recommend you wear a light jacket"
		elif(feelTempF >= 65):
			wear = "You won't need a jacket"
		#Umbrella
		umbrella = "Y"
		if(description == "mist" or description == "light rain" or description == "rain" or description == "heavy rain"):
			umbrella = "Y"
		else:
			umbrella = "N"
		print("The forecast is", description, "in", userCity, "this", time + ". The temperature is", tempF, "degrees Fahrenheit, with", humidity + "% humidity and a feels-like temperature of", feelTempF, "degrees Fahrenheit. We've got some", windDescription, "with the wind speed at", MPH, "MPH.", wear, "today.")
		if(umbrella == "Y"):
			print("Don't forget to bring an umbrella.")
		weather = input("Would you like to hear about the weather somewhere else? Y/N ")
	print("Have a great day!")

main()
