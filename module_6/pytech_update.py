#Setup connection to MongoDB
from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.ekjbea9.mongodb.net/pytech"
client = MongoClient(url)
db = client.pytech

#Find all "students" method
docs = db.students.find({})
#Display for all student documents
print("\n-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
for doc in docs:
    print("Student ID: " + doc["student_id"] + "\nFirst Name: " + doc["first_name"] + "\nLast Name: " + doc["last_name"] +"\n")

#Update one "student" method
update = db.students.update_one({"student_id": "1007"}, {"$set": {"last_name": "appleseed"}})

#Short list of students to make queries easier
john = db.students.find_one({"student_id": "1007"})
jane = db.students.find_one({"student_id": "1008"})
korbyn = db.students.find_one({"student_id": "1009"})

#Display for 1 query of student
print("\n-- DISPLAYING STUDENT DOCUMENT " + john["student_id"] + " --")
print("Student ID: " + john["student_id"] + "\nFirst Name: " + john["first_name"] + "\nLast Name: " + john["last_name"] +"\n")
input("\nEnd of program, press any key to exit... ")