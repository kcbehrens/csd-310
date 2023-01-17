from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.ekjbea9.mongodb.net/pytech"
client = MongoClient(url)
db = client.pytech

john = {
    "student_id": "1007",
    "first_name": "john",
    "last_name": "doe"
}

jane = {
    "student_id": "1008",
    "first_name": "jane",
    "last_name": "smith"
}

korbyn = {
    "student_id": "1009",
    "first_name": "korbyn",
    "last_name": "behrens"
}

print("\n-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

john_student_id = db.students.insert_one(john).inserted_id

print("Inserted student record john doe into the students collection with document_id " + str(john_student_id))

jane_student_id = db.students.insert_one(jane).inserted_id

print("Inserted student record jane smith into the students collection with document_id " + str(jane_student_id))

korbyn_student_id = db.students.insert_one(korbyn).inserted_id

print("Inserted student record korbyn behrens into the students collection with document_id " + str(korbyn_student_id))

input("\nEnd of program, press any key to exit... ")