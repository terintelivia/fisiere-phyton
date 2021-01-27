with open ("lista1.txt",'r') as f:
    x=f.readline()
    x.sort()
    print(x)
    x=str(x)
with open ('lista sortata.txt','w') as f:
    f.write(str(x))