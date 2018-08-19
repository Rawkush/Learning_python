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


def f(m):
    if m == 0:
      return(0)
    else:
      return(m+f(m-1))

print(f(10))



















    


