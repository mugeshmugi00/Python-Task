# import mongodb
import pymongo
from bson.objectid import ObjectId
# connect the mongodb to python file
myClient = pymongo.MongoClient("mongodb://localhost:27017")
# creating database name
myDB = myClient["studentManagementSystem"]
# creating collection name
myCollection = myDB["userRegister"]

# create user
# def create_user(name,mobile):
#     user = { 'name': name, 'mobile':mobile}
#     result = myCollection.insert_one(user)
#     print( result.inserted_id)
# create_user("exname",123456668)

newData = [
    {
        "name": "John Doe",
        "mobile": "+1-555-123-4567"
    },
    {
        "name": "Jane Smith",
        "mobile": "+44-7700-900123"
    },
    {
        "name": "Michael Johnson",
        "mobile": "+91-9876543210"
    },
    {
        "name": "Emily Brown",
        "mobile": "+61-412-345-678"
    },
    {
        "name": "David Wilson",
        "mobile": "+81-90-1234-5678"
    },
    {
        "name": "Sophia Martinez",
        "mobile": "+34-612-345-789"
    },
    {
        "name": "Liam Garcia",
        "mobile": "+1-555-987-6543"
    },
    {
        "name": "Olivia Lee",
        "mobile": "+82-10-9876-5432"
    },
    {
        "name": "Noah Davis",
        "mobile": "+27-71-234-5678"
    },
    {
        "name": "Isabella Clark",
        "mobile": "+33-6-12-34-56-78"
    }

]
# insert many
# def creat_Mul_User(user):
#    result = myCollection.insert_many(user)
#    print(result.inserted_ids)
# creat_Mul_User(newData)    

# find
# def getAllData():
#     result = myCollection.find()
#     for i in result:
#         print(i)
# getAllData()    

# find one id
# def getUserby_ID(userId):
#     newVar = ObjectId(userId)
#     result = myCollection.find_one({"_id":newVar})
#     print(result)
# getUserby_ID("670f5586e3839ccc5aca8e29")  

# find name by user
# def get_userName(userName):
#     result = myCollection.find_one({"name":userName})
#     print(result)
# get_userName("Jane Smith")    
    
    

