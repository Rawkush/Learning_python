marksheet=[]
for _ in range (int(input())):

    name=input()
    score=float(input())
    marksheet.append([name,score])

print(marksheet)

from operator import itemgetter

marksheet.sort(key=itemgetter(1))
print(marksheet)

print(marksheet[0],marksheet[1])
