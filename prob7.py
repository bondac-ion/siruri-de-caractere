s=str(input("Dati un sir de caractere:"))
s=s.upper()

nr=0
for i in range(0,len(s)):
    if s[i]=="A":
        nr+=1
s1=list(s)
print("numarul aparitiilor caracterului A este:",nr)
for i in range(0,len(s)):
    if s1[i]=="A":
        s1[i]="*"
a=""
for i in s1:
    a+=i
print("Sirul obtinut prin substituirea caracterului A cu *:",a)
s2=list(s)
d=[]
for i in range(0,len(s2)):
    if s2[i]!="B":
        d.extend(s2[i])
b=""           
for i in d:
    b+=i
print("Sirul obtinut prin radierea tuturor aparitiilor caracterului B din sirul S:",b)
t=0
for i in range(0,len(s)-1):
    if s[i]=="M" and s[i+1]=="A":
        t+=1
print("Numarul aparitiilor silabei MA este:",t)
s3=list(s)
for i in range(0,len(s3)-1):
    if s3[i]=="M" and s3[i+1]=="A":
        s3[i]="T"
        s3[i+1]="A"
c=""
for i in s3:
    c+=i
print("Sirul obtinut prin substituirea tuturor aparitiilor silabei MA din sirul S cu silaba TA",c)
d=list(s)
s5=s.replace("TO","") 
print("Sirul obtinut prin radeierea tuturor aparitiilor silabei TO din sirul S:",s5)
d.reverse()
s6=""
for i in d:
    s6+=i
print("Scrierea inversa a sirului S:",s6)