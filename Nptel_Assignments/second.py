def transpose(m):
  l=m
  c=l[0]
  lenght=len(c)
  x=0
  temp=[]
  new=[]
  for i in range(lenght):
  	
      for d in l:
          temp.append(d[i])
      
      new.append(temp)
      temp=[]
  return(new)

#next one


def descending(list):
    flag=0
    if(len(list)is 0):
        return True
    else:
        for i in range(0,len(list)):
            if(i>0 and list[i]<=list[i-1]):
                flag=flag+1
            
    if(flag is (len(list)-1)):
        return True
    else:
        return False


#next one


def valley(list):
    n=len(list)
    loc=list.index(min(list))
    
    if(n<5):
        return False
    elif(n is 0):
        return True
    flag=0
    flag1=0
    
    for i in range(0,n-1):
            if(list[i+1]<list[i] and i<loc):
                flag=flag+1
               

            elif(list[i]>list[i-1] and i>loc):
                flag1=flag1+1
            elif(list[i] is list[i+1]):
                return False
            
            else:
                flag1=flag1+1
                flag=flag+1
                
    if(list[n-1]>list[n-2] and list[n-1]>list[loc]):
        flag1=flag1+1
    elif(list[n-1]>list[n-2] and list[n-1]<=list[loc]):
        flag=flag+1
        
    if(flag>=2 and flag1>=2):
        return True
