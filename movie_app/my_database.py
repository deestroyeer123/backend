import pyrebase
from .models import Profile
from .serializers import ProfileSerializer
import json

config = {
  "apiKey": "apiKey",
  "authDomain": "projectId.firebaseapp.com",
  "databaseURL": "https://movieapplication-248de.firebaseio.com",
  "storageBucket": "projectId.appspot.com",
  "serviceAccount": "movie_app/firebase_sdk.json"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

class DatabaseHelper():

    tabele_name = "Profiles"

    def insert():
        profile = Profile(name="stefan", age=55, sex="facecik", movie1="filmik", movie2="elo", movie3="siema", elem1="elemencik", 
        elem2="drugi", elem3="trzeci", place="plaza", country1="francja", country2="polska", country3="niemcy", actor1="pierwszy", 
        actor2="aktorek", actor3="aktorzyna", director1="rezyserek", director2="albert", director3="piotrus", is_ocar_winning=True, 
        years1="wczesne", years2="srednie", years3="pozne", food1="chrupki", food2="jedzonko", food3="piwko", group="mala")
        serializer = ProfileSerializer(profile)
        db.child("Profiles").push(serializer.data)

    def insert2(values):
        db.child("Profiles").push(values)

    def update():
        user = db.child("Profiles").get()
        print(user)
        #DatabaseHelper.insert()
        #db.child("Profiles").child("Morty").update({"name": "Mortiest Morty"})
        