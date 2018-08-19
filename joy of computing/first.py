def intreverse(n):
    st=str(n)
    temp=""
    for var in st:
        temp=var+temp

    n=int(temp)
    return n

#second function

def matched(s):
    x=0
    y=0
    for var in s:
        if var=="(":
            x=x+1           
            
        if var==")":
            y=y+1
            if y>x:
                return False

    if x==y:
        return True
    else:
        return False

# 3rd function

def sumprimes(l):
    s=0
    for var in l:
        if var>0:
            if prime(var):
                s=s+var
    return s

def prime(num):
    for i in range(2, int(num/2)+1):
        if num%i== 0:
            return False;
            break
    return True



def test(n):
	if n%7==0:
		print('Hipp Hipp Hurrah')
	else:
		print('Alas')




for i in range(11,16):
	if i%2==0:
		print('Jack')
	elif i%3==0:
		print('Jill')
	elif i%2==0 and i%3==0:
		print('Jack and Jill')
	else:
		print('Jill and Jack')




list_1=[]
for i in range(1,51):
  list_1.append(i)
  
a, b = input().split()

a=int(a)
b=int(b)

list_1[a:b]

for i in list:
  print(i)





















            
