t=()
while 1:
           item = input('Enter the item')
           t=t+(item,)
           c=input('Do you want to continue Y/N')
           if c.lower()=='n':
                          break
print(t)
