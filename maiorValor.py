n = int(input())
m = int(input())
s = int(input())
resp = -1
for j in range(m,n):
    algarismos = str(j)
    soma=0
    i=0
    for i in range(len(algarismos)):
        soma+=int(algarismos[i])
        print("oi")
    if(soma==s):
        resp=j
        break
print(resp)