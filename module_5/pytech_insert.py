from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.ekjbea9.mongodb.net/pytech"
client = MongoClient(url)
db = client.pytech

john = { "name" : "John", "student_id" : "1007" }
john_student_id = db.students.insert_one(john).inserted_id
print(john_student_id)