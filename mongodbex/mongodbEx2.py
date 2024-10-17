import pymongo
from bson.objectid import ObjectId
# connect the file mongodb mongodb://localhost:27017/
connection = pymongo.MongoClient("mongodb://localhost:27017")
# creat db
DataBase = connection["userDataExample"]
# creat collection
collection = DataBase["personsDet"]

# # cerat user
# userOne = {
#         "name": "Isabella Clark",
#         "mobile": "+33-6-12-34-56-78"
#     }
# # insert one
# def userDataOne(userData):
#     result = collection.insert_one(userOne)
#     print(result)
# userDataOne(userOne)

# # insert many
# manypersonData = [
#     {
#         "name": "Ava Turner",
#         "mobile": "+1-555-234-7890"
#     },
#     {
#         "name": "Ethan Roberts",
#         "mobile": "+44-7712-123456"
#     },
#     {
#         "name": "Mia Walker",
#         "mobile": "+49-151-23456789"
#     },
#     {
#         "name": "James Thompson",
#         "mobile": "+1-555-345-6789"
#     },
#     {
#         "name": "Charlotte Harris",
#         "mobile": "+61-488-123-456"
#     },
#     {
#         "name": "Lucas Clark",
#         "mobile": "+86-138-1234-5678"
#     },
#     {
#         "name": "Amelia King",
#         "mobile": "+33-6-11-22-33-44"
#     },
#     {
#         "name": "Henry Young",
#         "mobile": "+1-555-567-8901"
#     },
#     {
#         "name": "Harper Scott",
#         "mobile": "+91-98765-43210"
#     },
#     {
#         "name": "William Carter",
#         "mobile": "+27-72-987-6543"
#     }
# ]
# # insert many
# def userDatamany(manyUsers):
#     result = collection.insert_many(manyUsers)
#     print(result)
# userDatamany(manypersonData)

# # find()
# def getPersonsData_All():
#     result = collection.find()
#     for i in result:
#         print(i)
# getPersonsData_All()    

# # find one()
# def getdataOne(personID):
#     dataOne = ObjectId(personID)
#     result = collection.find_one({"_id":dataOne})
#     print(result)
# getdataOne("670f5f6e16bf9bda67ef8a85")    

# 17-10-2024
# update one()
# getName = {"name":"Isabella Clark"}
# setName = {"$set":{"name":"mugesh"}}
# def updateUser_Data(oldData,newData):
#     result = collection.update_one(oldData,newData)
#     print(result)
# updateUser_Data(getName,setName)

# limit()
# pipelione = [
#     {"$limit":5}
# ]
# def limitedData(limitData):
#     result = collection.aggregate(limitData)
#     for i in result:
#         print(i)
# limitedData(pipelione)    

# delete
# def detetData(userDataID):
#     newVar = ObjectId(userDataID)
#     result = collection.delete_one({"_id":newVar})
#     print(result)
# detetData("670f5e83e02fc5bfc022e3f2")    

# sorting asending
# userName = [{"$sort":{"name":1}}]
# def assendingData(nameData):
#     result = collection.aggregate(nameData)
#     for i in result:
#         print(i)
# assendingData(userName)    


# userData = [
#     {
#         "_id": 1,
#         "name": "Alice",
#         "department": "HR",
#         "salary": 50000
#     },
#     {
#         "_id": 2,
#         "name": "Bob",
#         "department": "IT",
#         "salary": 70000
#     },
#     {
#         "_id": 3,
#         "name": "Charlie",
#         "department": "IT",
#         "salary": 80000
#     },
#     {
#         "_id": 4,
#         "name": "David",
#         "department": "Finance",
#         "salary": 60000
#     }
# ]
# def sameData(pipeline):
#     display = collection.insert_many(pipeline)
#     print(display)
# sameData(userData)

# match()
# def matchData():
#     pipeline = [
#         {
#             "$match": {
#                 "department": "IT",           
#                 "salary": {"$gt": 60000}     
#             }
#         }
#     ]
#     result = collection.aggregate(pipeline)
#     for i in result:
#         print(i)
# matchData()

# 
