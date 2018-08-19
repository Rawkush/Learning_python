a='"hello' # enclosing " inside ' will treat " as a part of string

b=' ankush"'

print(a+b)  # + will concatenate the string


#repeting a string

print(a*5) #it will rerpeat string a 5 times

# fetching a specific character in string

print(a[2])

#fetching a range of chafracter from string

print(a[1:3])



#checking is a specific part of string is present or not


'hel' in a  #Checks if the character 'hel' is present in the string and returns true or false


# we can do fill in the blan type problem with 'string
# that a data can late be entered in between the string
#like we do in C in printf function



ball='basketball'
ball2='football'
print('i have a %s, lets play with it',%ball)

print(' the two ball  %s that i have are stolen',%(ball,ball2))


#to find where a specific substring is in a string


var='learning python seems easy'

var.find('ing')

#counting the occurenece  of a substring

var.count('n')













