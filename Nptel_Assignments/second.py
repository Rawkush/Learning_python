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
