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
    print(num)

    for i in range(2, int(num/2)+1):
        print(num%i)

        if num%i== 0:
            return False;
            break
    return True






























            
