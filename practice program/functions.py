def g(x):

    (q,d) = (1,0)
    while q <= x:
        
        (q,d) = (q*10,d+1)
    return(d)

print(g(31415927))


def h(m,n):
    ans = 0
    while (m >= n):
      (ans,m) = (ans+1,m-n) 
    return(ans)

print(h(231,8))

# composite number program
def h(n):
    f = 0
    for i in range(1,n+1):
      if n%i == 0:
        f = f + 1
    return(f%2 == 1)

print(h(4))

# n(n+1)/2 using recursion
def f(m):
    if m == 0:
      return(0)
    else:
      return(m+f(m-1))

print(f(10))


#

x = [1,"abcd",2,"efgh",[3,4]]  # Statement 1
y = x[0:50]                    # Statement 2
z = y                          # Statement 3
w = x                          # Statement 4
x[1] = x[1] + 'd'              # Statement 5
y[2] = 4                       # Statement 7
z[0] = 0                       # Statement 8
w[4][0] = 1000                 # Statement 9
a = (x[4][1] == 4)             # Statement 10



x = [13,4,17,1000]
w = x[1:]
u = x[1:]
y = x
u[0] = 50
y[1] = 40


print(x[1])
print(y[1])
print(w[0])
print(u[0])


#reversing the string
startmsg = "hello"
endmsg = ""
for i in range(0,len(startmsg)):
      endmsg = startmsg[i] + endmsg
print(endmsg)


def mystery(l):
    l = l + l
    return()

mylist = [31,24,75]
mystery(mylist)
print(mylist)




    


