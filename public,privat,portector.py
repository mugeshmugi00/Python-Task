# protector
class ClassA:
    _password=12365468
    def __init__(self,name):
        self.name=name
    def givenPass(self):
        print(self._password)    
    def setPassword(self,password):
        self._password=password
class ClassB(ClassA):
    def __init__(self):
        pass
objB=ClassB()
objB.setPassword("23145687") 
# objB.givenPass()     

# privat
class ClassA:
    __password=12365468
    def __init__(self,name):
        self.name=name
    def givenPass(self):
        print(self.__password)    
    def setPassword(self,password):
        self.__password=password
class ClassB(ClassA):
    def __init__(self):
        pass
objB=ClassB()
objB.setPassword("145687") 
# objB.givenPass() 


class Parent:
    father="appa"
    mother="amma"
    __fatherPass=""
    _motherPass=""
    # consterctor
    def __init__(self,father,mother):
        self.father=father
        self.mother=mother
    def parentsDetieals(self):
        print(self.father,self.mother)
        # print("parent")
    def setPass(self,fatherPass,motherPass):
        self.__fatherPass=fatherPass
        self._motherPass=motherPass
    def givePassword(self):
        print(self.__fatherPass,self._motherPass)
class Chiled(Parent):
    def __init__(self):
        pass
chil1=Chiled()
chil1.setPass(321654,654987)
chil1.parentsDetieals()
chil1.givePassword()                    




