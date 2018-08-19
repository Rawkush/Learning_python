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




