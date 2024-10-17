import os
import json
data = [{"name":"mukesh","age":24,"phone":645564653},{"name":"dinesh","age":24,"phone":654654}]
# newData = {'name': 'fsadfasd', 'age': 5674, 'phone': 8674}

# data.append(newData)
# print(data)
# file = "datas.json"
# print(os.path.exists(file))
def checkFile(filename):
    if(os.path.exists(filename)):
        return True
    else:
        return False
        
        
def createFile(filename):
    res = checkFile(filename)
    if(res):
        print("this file is already exists")
    else:
        file = open(filename,"x")
        file.close()
        print("file is created successfully")
        
createFile("datas.json")

def writeFile(filename):
    res = checkFile(filename)
    if(res):
        with open(filename,"w") as file:
            file.write(json.dumps(data,indent=2))
    else:
        print("ther is no file")
        createFile(filename)
        print('write successfully')
writeFile("datas.json") 
       
def readFile(filename):
    with open(filename,"r") as file:
        data = file.read()
        # print(type(data))
        convData = json.loads(data)
        # print(type(convData))
        return convData
    
def appendFile(filename):
    name = input("enter name: ")
    age = int(input("enter age: "))
    phone = int(input("enter phone number: "))
    d = {"name":name,"age":age,"phone":phone}
    newData = readFile(filename)
    newData.append(d)
    with open(filename,"w") as file:
        file.write(json.dumps(newData,indent=2))
        # print(type(newData))
# writeFile("datas.json")
# appendFile("datas.json")


def updateFile(filename):
    newdata1=writeFile(filename)
    for person in data:
        if(person["name"] == "mukesh"):
            person["age"]=21
    readFile(filename)
    newdata1.append(data)

    print(data) 
updateFile("datas.json")


