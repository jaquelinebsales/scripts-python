a = int(input("Digite um número inteiro qualquer: "))

print("SOMA")
for i in range(1,11):
    print(f"{a}+{i}={a+i}")
print("SUBTRAÇÃO")
for i in range(1,11):
    print(f"{a}-{i}={a-i}")
print("MULTIPLICAÇÃO")
for i in range(1,11):
    print(f"{a}x{i}={a*i}")
print("DIVISÃO")
for i in range(1,11):
    print(f"{a}/{i}={a/i:=.2f}")