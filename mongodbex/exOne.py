import pymongo
from bson.objectid import ObjectId
# connecting mongo db URL
myClient = pymongo.MongoClient("mongodb://localhost:27017")
# creating database
mydb = myClient["python_database"]

# creating collection
mycol = mydb['users']

#insert data
##def create_user(name, age):
##    user = {'name': name, 'age': age}
##    result = mycol.insert_one(user)
##    return result.inserted_id
##
##create_user("Gowtham",17)

# insert_many

##users = [
##    {"name": "Alice", "age": 30, "email": "alice@example.com"},
##    {"name": "Bob", "age": 25, "email": "bob@example.com"},
##    {"name": "Charlie", "age": 35, "email": "charlie@example.com"},
##    {"name": "David", "age": 40, "email": "david@example.com"},
##    {"name": "Eva", "age": 22, "email": "eva@example.com"}
##]
##
##def insertMultipleUser(usersData):
##    insertData = mycol.insert_many(usersData)
##    return insertData.inserted_ids
##insertMultipleUser(users)

# get all data from collection

##def getAllUser():
##    allUser = mycol.find()
##    for userData in allUser:
##        print(userData)
##
##getAllUser()

# get specific user

##def getSpecificUser(id):
##    objId = ObjectId(id)
##    myDocument = mycol.find_one({"_id":objId})
##    print(myDocument)
##
##getSpecificUser("66c495dc8c1dd9087adfcb49") 

# update data

##findRecord = {"name":"Gowtham"}
##newValue = {"$set":{"name":"jaiseelan"}}
##def updateData(query,newData):
##    updateRecord = mycol.update_one(query,newData)
##
##updateData(findRecord,newValue)

# $limit

##pipeline = [
##    { '$limit': 10 }
##    ]
##def getDataLimit(Countlimit):
##    limitedData = mycol.aggregate(Countlimit)
##    for document in limitedData:
##        print(document)
##getDataLimit(pipeline)

# $sort  1 for ascending, -1 for descending

# pipeline = [{"$sort":{"age":1}}]
##nameSort = [{"$sort":{"name":1}}]
##def getData(sortType):
##    result = mycol.aggregate(sortType)
##    for doc in result:
##        print(doc)
##getData(nameSort)

# get all data greater than age 25
# query = { 'age': { '$gt': 25 } }
# def getData(queryData):
#     result = mycol.find(queryData)
#     for doc in result:
#         print(doc)
# getData(query)