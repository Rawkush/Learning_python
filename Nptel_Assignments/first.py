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

