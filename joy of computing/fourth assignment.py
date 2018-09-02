a,b=input().split()
a=int(a)
b=int(b)
k=1
c=1
for i in range(a):
  for j in range(b):
         
    print(k,end="")
    if c<b:  
      print(" ",end="")
    c+=1
    k+=1
  c=1  
  print()

###NEXT

num=int(input())
factorial=1
if num == 0:
   print("1")
else:
  
  for i in range(1,num + 1):
    
    factorial = factorial*i
  print(factorial)

###nEXT

n=int(input())
p=[]
for i in range(n):
  p.append(int(input()))
p.sort()
for i in range(n):
  print(p[i],end=" ")
