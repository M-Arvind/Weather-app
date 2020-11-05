from tkinter import *
from PIL import ImageTk, Image
import requests
import json

root = Tk()
root.title("Weather App")
root.geometry("600x100")

def ziplookup():

    try:
        API_REQUEST = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + Zip.get() + "&distance=5&API_KEY=EA18ECEE-94A9-4286-870B-F2A315F6865F")
        API = json.loads(API_REQUEST.content)
        CITY = API[0]['ReportingArea']
        QUALITY = API[0]['AQI']
        CATEGORY = API[0]['Category']['Name']

        if CATEGORY == "Good":
            weather_color = "#0C0"
        if CATEGORY == "Moderate":
            weather_color = "#FFFF00"
        if CATEGORY == "Unhealthy fot sensitive groups":
            weather_color = "#ff9900"
        if CATEGORY == "Unhealthy":
            weather_color = "#FF0000"
        if CATEGORY == "Very Unhealthy":
            weather_color = "990066"
        if CATEGORY == "Hazardous":
            weather_color = "660000"

        root.configure(background=weather_color)

        mylabel  = Label(root, text=str(CITY) + " Air Quality " + str(QUALITY) + "  "  + str(CATEGORY), font=("Times New Roman", 20), background = weather_color)
        mylabel.grid(row=1, column=0)

    except Exception as e:
        API = "Error..."

Zip = Entry(root)
Zip.grid(row=0, column=0, sticky=W+E+N+S)

zipbutton = Button(root, text="lookup zipcode", command=ziplookup)
zipbutton.grid(row=0, column=1, sticky=W+E+N+S)

root.mainloop()
