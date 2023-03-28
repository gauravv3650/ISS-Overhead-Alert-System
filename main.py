import requests
from datetime import datetime
import smtplib
import time
import os

my_email = "newemailjustforproject@gmail.com"
password = "atcbbgmbgwazjkje"


MY_LAT = 19.020490
MY_LONG = 73.003600


def issOverhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    longitude = float(data["iss_position"]["longitude"])
    latitude = float(data["iss_position"]["latitude"])

    if MY_LAT - 4 <= latitude <= MY_LAT + 4 and MY_LONG - 4 <= longitude <= MY_LONG + 4:
        return  True


def itsNight():
     current_time= datetime.now().hour
     parameters = {
         "lat": MY_LAT,
         "long": MY_LONG,
         "formatted": 0
     }
     response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
     response.raise_for_status()
     data = response.json()

     print(data)
     sunrise = int(data['results']["sunrise"].split("T")[1].split(":")[0])
     sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

     if  sunset < current_time < sunrise:
         return  True


while True:
    time.sleep(60)
    if issOverhead() and itsNight() == True:


        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email,password=password)
            connection.sendmail(from_addr=my_email,to_addrs="gaurav.mishra3650@gmail.com",
                                msg=f"Subject:Iss\n\n is above you head gaurav go and watch in the sky😉 ")
