from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

def getWeather():
    city = textfield.get()

    if not city:
        messagebox.showerror("Error", "Please enter a city name!")
        return

    try:
    #Geolocation setup
        geolocator= Nominatim(user_agent="my_weather_app")
        location= geolocator.geocode(city)

        if location is None:
            messagebox.showerror("Error", "City not found!")
            return
        
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude,lat=location.latitude)
        
        home=pytz.timezone(result)
        local_time=datetime.now(home)
        current_time=local_time.strftime("%I:%M:%p")
        clock.config(text=current_time)
        name.config(text="CURRENT WEATHER")

        #API Call
        api=api = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=c029e98d32717996840b0cc17c06d40c"

        json_data = requests.get(api).json()

        #Extract weather data
        condition = json_data['weather'][0]['description']
        temp = int(json_data['main']['temp'] - 273.15)
        humidity = json_data['main']['humidity']
        pressure = json_data['main']['pressure']
        wind = json_data['wind']['speed']

        t.config(text=(temp,"\u00B0C"))
        c.config(text=f"{condition.capitalize()} | FEELS LIKE  {temp}\u00B0C")
        w.config(text=f"{wind} m/s")
        h.config(text=f"{humidity}%")
        p.config(text=f"{pressure} hPa")
        d.config(text=condition.capitalize()) 

    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong: {e}")

root = Tk()
root.title("Wheather App")
root.geometry("900x500+300+200")
root.resizable(True, True)

#search box
Search_image=PhotoImage(file="D:/PythonProject/Weather/search.png")
myimage=Label(image=Search_image)
myimage.place(x=20, y=20)
textfield=tk.Entry(root,justify="center", width=17, font=("poppins", 25, "bold"), bg="#404040", border=0, fg="White")
textfield.place(x=50, y=40)
textfield.focus()

#Bind Enter Key to search function
textfield.bind("<Return>", lambda event: getWeather())

#search icon
Search_icon=PhotoImage(file="D:/PythonProject/Weather/search_icon.png")
myimage_icon=Button(image=Search_icon, borderwidth=0, cursor="hand2", bg="#404040",command=getWeather)
myimage_icon.place(x=400, y=34)

#logo
Logo_image=PhotoImage(file="D:/PythonProject/Weather/logo.png")
logo=Label(image=Logo_image)
logo.place(x=150, y=100)

#Bottom box
Bottom_image=PhotoImage(file="D:/PythonProject/Weather/box.png")
bottom_myimage=Label(image=Bottom_image)
bottom_myimage.pack(padx=5,pady=5,side=BOTTOM)

#Time
name=Label(root,font=("arial",15,"bold"))
name.place(x=30,y=100)
clock=Label(root,font=("Helvetica",20))
clock.place(x=30,y=130)

#label
label1=Label(root,text="WIND", font=("Helvetica", 15, 'bold'),fg="White", bg="#1ab5ef")
label1.place(x=115, y=400)

label2=Label(root,text="HUMIDITY", font=("Helvetica", 15, 'bold'),fg="White", bg="#1ab5ef")
label2.place(x=250, y=400)

label3=Label(root,text="DESCRIPTION", font=("Helvetica", 15, 'bold'),fg="White", bg="#1ab5ef")
label3.place(x=425, y=400)

label4=Label(root,text="PRESSURE", font=("Helvetica", 15, 'bold'),fg="White", bg="#1ab5ef")
label4.place(x=660, y=400)

#Temp
t=Label(font=("arial",70,"bold"),fg="#ee666d")
t.place(x=400,y=150)

#Condition
c=Label(font=("arial",15,'bold'))
c.place(x=400,y=250)

#Wind
w=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
w.place(x=120,y=430)

#Humidity
h=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
h.place(x=270,y=430)

#Description
d=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
d.place(x=430,y=430)

#Pressure
p=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
p.place(x=670,y=430)

root.mainloop()