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
x[1][1] = 'y'                  # Statement 6
y[2] = 4                       # Statement 7
z[0] = 0                       # Statement 8
w[4][0] = 1000                 # Statement 9
a = (x[4][1] == 4)             # Statement 10






















    


