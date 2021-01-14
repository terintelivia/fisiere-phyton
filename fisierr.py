with open('input.txt1','r') as f:
    sir=f.readline()
ma=0
mi=0
c=0
o=0
for i in s:
    if ord(i) in range (65,91):
    ma+=1
with open('litereA.txt','w') as f:
    f.write(str(ma))
for i in sir:
    if ord(i) in range (97,123):
    mi+=1
with open ('litereB.txt','w') as f:
    f.write(str(mi))
for i in sir:
    if ord(i) in range (48,58):
    c+=1
with open('cifre.txt','w') as f:
    f.write(str(c))
for i in  sir:
    if ord(i) in range (33,48) or ord(i) in range (58,65) or ord(i) in range (91,97) or ord(i) in range (123,128):
    o+=1
with open('operatori.txt','w') as f:
    f.write(str(o))