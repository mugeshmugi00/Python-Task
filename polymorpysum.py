class Shap:
    lenth=""
    breadth=""
    radius=""

    def __init__(self,lenth,breadth,radius):
        self.lenth=lenth
        self.breadth=breadth
        self.radius=radius
    def calculatArea(self):
        pass
class Rectangul(Shap):
    def __init__(self,lenth,breadth):
        self.lenth=lenth
        self.breadth=breadth
    def calculatArea(self):
        print("lenth and breadth valus are:",self.lenth*self.breadth) 
r1=Rectangul(100,100)
r1.calculatArea()
class Circule(Shap):
    pi=3.14
    def __init__(self,radius):
        # self.pi=pi
        self.radius=radius 
    def calculatArea(self):
        print("circule of area:",self.pi*self.radius*2)
c1=Circule(10)
c1.calculatArea()        