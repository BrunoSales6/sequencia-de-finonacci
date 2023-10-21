n=int(input("Quantos números você quer gerar?"))
if n<=0:
    print("Digite um número positivo")
elif n==1:
    print(1)
elif n==2:
    print(1, 1)
else:
    print("1 1", end=" ")
    a,b=1,1
    for c in range(2,n):
        a,b=b,a+b
        print(b, end=" ")
 