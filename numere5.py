#	Afişaţi tabla înmulţirii cu numărul n. Exemplu: pentru n=5, se va afişa pe verticală 1x5=5  2x5=10 3x5=15 4x5=20 5x5=25 6x5=30 7x5=35 8x5=40 9x5=45 10x5=50. 
#Din fişierul « numar.txt » se citeşte un număr, în fişierul « inmultire.txt » - se înscrie tabla înmulţirii cu acest număr.

with open('numar.txt','r') as f:
  n=f.readline()
for i in (1,10):
    x=str(i)+'*'+n+'='+str(i*int(n))
with open('inmultire.txt','w') as f:
    f.write(str(x))
    f.write(str(' '))
    
