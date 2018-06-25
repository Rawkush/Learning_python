#syntax of class
class className:
    name="ankush"
    gender="male"
    def ShowInfo(self): #method in class
        print('NAme:',self.name)
        print('gender',self.gender)



#outside of class now

p1=className()
p1.ShowInfo()


#creating a class which initialisees the data members from user input


class person:
    def __init__(self,a='ravi',b='male'):
                 self.name=a
                 self.gender=b
    def ShowInfo(self):
                 
                 print('NAme:',self.name)
                 print('gender',self.gender)




p2=person('ank','male')
p2.ShowInfo()
