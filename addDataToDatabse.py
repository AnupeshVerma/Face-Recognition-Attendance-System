import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://faceattendance-84fa9-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "20205039":
        {
            "name": "Anupesh Kumar Verma",
            "major": "Electronics",
            "starting_year": 2020,
            "total_attendance": 7,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "20205136":
        {
            "name": "Samriddhi Dhiraj",
            "major": "Electronics",
            "starting_year": 2020,
            "total_attendance": 12,
            "standing": "B",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "963852":
        {
            "name": "Elon Musk",
            "major": "Physics",
            "starting_year": 2020,
            "total_attendance": 7,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2022-12-11 00:54:34"
        }
}

for key, value in data.items():
    ref.child(key).set(value)