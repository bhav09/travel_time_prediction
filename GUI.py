'''
The model here is trained on a 2016 based Nwe York City's dataset. So will be entering the places of new york city itself.
'''
from tkinter import *
from PIL import Image
from geopy.geocoders import Nominatim
import pandas as pd
import joblib

regressor = joblib.load('finalized_model (1).sav')

def predict():
    global y_pred,fetch_d,fetch_p

    fetch_p = pickup_entry.get()
    fetch_d = dropoff_entry.get()
    pickup()
    dropoff()
    dataframe()
    y_pred = regressor.predict(x_test)
    y_pred = int(y_pred/60)+2
    result = 'It will approximately take : '+(str(y_pred) + ' mins')
    pred_result = Label(root, text=result, bg='orange',fg='black',font=(15))
    pred_result.place(x=20, y=500)
def dataframe():
    global x_test
    dic ={'passenger_count': passenger.get() ,'pickup_longitude': pickup_longitude, 'pickup_latitude':pickup_latitude,
          'dropoff_longitude':dropoff_longitude,'dropoff_latitude':dropoff_latitude,'Day':3,'Total_Seconds':1468057545}
    x_test = pd.DataFrame([dic])

def pickup():
    global pickup_longitude , pickup_latitude
    geolocator_pickup = Nominatim()
    fetch = fetch_p
    fetch1 = fetch.split(',')
    place = fetch1[0]
    city = fetch1[1]
    loc = geolocator_pickup.geocode(place + ',' + city)
    print("pickup_latitude is : ", loc.latitude, "\npickup_longtitude is: ", loc.longitude)
    pickup_longitude = loc.longitude
    pickup_latitude = loc.latitude

def dropoff():
    global dropoff_latitude,dropoff_longitude
    geolocator_dropoff = Nominatim()
    fetch = fetch_d
    fetch = fetch.split(',')
    place = fetch[0]
    city = fetch[1]
    loc = geolocator_dropoff.geocode(place + ',' + city)
    print("dropoff_latitude is : ", loc.latitude, "\ndropoff_longtitude is: ", loc.longitude)
    dropoff_latitude = loc.latitude
    dropoff_longitude = loc.longitude

root = Tk()
root.title('Local Guide')
root.configure(background='light goldenrod yellow')
root.geometry('800x600')
root.resizable(0,0)

map = Image.open('map (2).png')
map = map.resize((120,120),Image.ANTIALIAS)
map = map.save('m.ppm','ppm')
map = PhotoImage(file='m.ppm')

welcome_image = Image.open('namaste.jpg')
welcome_image = welcome_image.resize((120,120),Image.ANTIALIAS)
welcome_image = welcome_image.save('namaste.ppm','ppm')
welcome_image = PhotoImage(file='namaste.ppm')

welcome = Label(root,text='Welcome to the Local Guide',font=(23),bg='light goldenrod yellow')
welcome.place(x=290,y=50)
map_label = Label(root,image=map,bg='black')
map_label.place(x=600,y=50)
namaste_label = Label(root,image=welcome_image,bg='black')
namaste_label.place(x=120,y=50)


current_location = Button(root,text='My Location',bg='orange')
current_location.place(x=610,y=200)

passenger_count = Label(root,text='No. of Passengers', bg='black',fg='white')
passenger_count.place(x=10,y=200)

passenger = Entry(root,bg='orange',justify='center')
passenger.place(x=120,y=200)

pickup_location = Label(root,text='Pick Up Location  ',bg='black',fg='white')
pickup_location.place(x=10,y=230)
pickup_entry = Entry(root,bg='orange',justify='center')
pickup_entry.place(x=120,y=230)

dropoff_location = Label(root,text='Drop off Location ',bg='black',fg='white')
dropoff_location.place(x=10,y=260)
dropoff_entry = Entry(root,bg='orange',justify='center')
dropoff_entry.place(x=120,y=260)


estimate_time = Button(text='CLICK TO PREDICT',bg='gold',fg='black',activebackground='orange',command=predict)
estimate_time.place(x=50,y=330)


credits = Label(root,bg='black',fg='white',text='©Developed by Bhavishya Pandit',height=3,width=120)
credits.place(x=0,y=550)

root.mainloop()

#entered inputs

#2
#Times Square,New York
#Central Park, New York