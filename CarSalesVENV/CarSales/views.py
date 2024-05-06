from django.shortcuts import render
from django.apps import apps
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

def connectDB():
    if not firebase_admin._apps:
        cred = credentials.Certificate("carsales-admin-key.json")
        firebase_admin.initialize_app(cred, {
            "databaseURL": "https://projectname-xxxxxxxxxxx-rtdb.firebaseio.com/" #Your database URL
        })
    dbconn = db.reference("CarsList")
    return dbconn

def carslist(request):
    cars = []
    dbconn = connectDB()
    tblCars = dbconn.get()
    for key, value in tblCars.items():
        cars.append({"id": value["ID"], "name": value["Name"], "year": value["Year"], "price": value["Price"]})
    return render(request, 'carslist.html', {'cars':cars})