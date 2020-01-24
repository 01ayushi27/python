a=input()
k=' '
for i in a:
     if i not in k:
            out = a.count(i)
            print(i, ':', out)
            k+=i
            
