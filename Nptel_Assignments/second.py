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
