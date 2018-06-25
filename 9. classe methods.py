class person:
    count=0 # class atrribute (similar to static members)
    #the variable is shared by all objects of class 
    def __init__(self,a='Ravi',b='Male'):
        self.name=a
        self.gender=b
        person.count= person.count+1
    def ShowInfo(self):
        print('name', self.name)
        print('gender', self.gender)

    @classmethod #mehod below it is class method
    #class method is similar to static methods in java    
    def ShowCount(cls):
        print('Number of objects created so far',cls.count)


p=person('ankush','male')
p2=person('rahul','male')
p3=person('manoj','male')

person.ShowCount()
