# creating a function

def function_name():
    "explainatory string ius wriiten here, it is smilar to comment" # it is optional
    print("created the function and inside the function cui=rrently")
    return
    
#global variable

age=17

def newFunction():
    age=12 ## this age is local variable
    print(age)
    return

newFunction()

print(age)

#to chanege the gl,obal variable

def changing():
    
    global qge
    age=12 ## this age is local variable
    print(age)
    return


changing()
print("global changed",age)
    
