from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.ekjbea9.mongodb.net/pytech"
client = MongoClient(url)
db = client.pytech

docs = db.students.find({})
print("\n-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
for doc in docs:
    print("Student ID: " + doc["student_id"] + "\nFirst Name: " + doc["first_name"] + "\nLast Name: " + doc["last_name"] +"\n")

john = db.students.find_one({"student_id": "1007"})
jane = db.students.find_one({"student_id": "1008"})
korbyn = db.students.find_one({"student_id": "1009"})

print("\n-- DISPLAYING STUDENTS DOCUMENTS FROM find_one() QUERY --")
print("Student ID: " + john["student_id"] + "\nFirst Name: " + john["first_name"] + "\nLast Name: " + john["last_name"] +"\n")
input("\nEnd of program, press any key to exit... ")