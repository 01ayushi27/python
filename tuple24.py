t=[1,2,3,(1,),4]
c=0
for i in t:
     if type(i)!=tuple:
              c+=1
     else:
              break
print(c)

