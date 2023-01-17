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

#Insert one "student" method
python = {
    "student_id": "1010",
    "first_name": "python",
    "last_name": "coder"
}
insert = db.students.insert_one(python).inserted_id
#Displays that an insert was made and who it is
print("\n-- INSERT STATEMENTS --")
print("Inserted student record into the students collection with document_id " + str(insert))

#Short list of students to make queries easier
john = db.students.find_one({"student_id": "1007"})
jane = db.students.find_one({"student_id": "1008"})
korbyn = db.students.find_one({"student_id": "1009"})
python = db.students.find_one({"student_id": "1010"})

#Display for 1 query of student
print("\n-- DISPLAYING STUDENT TEST DOC --")
print("Student ID: " + python["student_id"] + "\nFirst Name: " + python["first_name"] + "\nLast Name: " + python["last_name"] +"\n")

#Delete one "student" method
delete = db.students.delete_one(python)

#Find all "students" method
docs = db.students.find({})
#Display for all student documents
print("\n-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
for doc in docs:
    print("Student ID: " + doc["student_id"] + "\nFirst Name: " + doc["first_name"] + "\nLast Name: " + doc["last_name"] +"\n")

input("\nEnd of program, press any key to continue... ")