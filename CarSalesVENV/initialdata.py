import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("carsales-admin-key.json")
firebase_admin.initialize_app(cred, {
    "databaseURL": "https://sample-7440c-default-rtdb.asia-southeast1.firebasedatabase.app" #Your database URL
})

dbref = db.reference("CarsList")
dbref.push( { "ID": 1, "Name": "Toyota Camry", "Year": 2018, "Price": 2000 } )
dbref.push( { "ID": 2, "Name": "Honda Civic", "Year": 2019, "Price": 2200 } )
dbref.push( { "ID": 3, "Name": "Chevrolet Silverado", "Year": 2017, "Price": 1800 } )
dbref.push( { "ID": 4, "Name": "Ford F-150", "Year": 2020, "Price": 2500 } )
dbref.push( { "ID": 5, "Name": "Nissan Altima", "Year": 2021, "Price": 3000 } )

print(dbref.get())