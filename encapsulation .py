class ClassA:
    def __init__(self,name,age):
        self.personName=name
        self.personAge=age
    def giveStudentDetieals(self):
        print(self.personName,self.personAge)

class ClassB(ClassA):
    def __init__(self,name,age,mobileNo):
        super().__init__(name,age)
        self.personMobileNo=mobileNo
    def get(self):
        super().giveStudentDetieals()
objB=ClassB("mugesh",21,21984654654)
objB.get()
