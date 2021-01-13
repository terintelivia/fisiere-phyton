#	Ion şi Vasile joacă următorul joc: Ion spune un număr iar Vasile trebuie să găsească cinci numere consecutive, crescătoare, numărul din mijloc fiind cel ales de Ion. 
#Exemplu : Ion spune 10, Vasile spune 8 9 10 11 12. Ajutaţi-l pe Vasile să găsească răspunsul mai repede. Din fişierul « input.txt » se citeşte un număr, în fişierul « output.txt » - se înscrie consecutivitatea numerelor.

with open('input.txt','r') as f:
    a=f.readline()
    x= str(int(a)-2)+" " + str(int(a)-1)+ " " + str(int(a))+ " " + str(int(a)+1)+ " " + str(int(a)+2)
with open('ouput.txt','w') as f:
    f.write(str(x))