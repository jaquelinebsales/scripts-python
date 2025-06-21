#informações

a = input("Digite algo: ")

print("O tipo primitivo desse valor é: ", type(a))
print("Só tem espaços? ", a.isspace())
print("É um número? ", a.isnumeric())
print("É alfabético? ", a.isalpha())
print("É alfanumérico? ", a.isalnum())
print("É maiúsculo? ", a.isupper())
print("É minúsuclo? ", a.islower())
print("É capitalizado? ", a.istitle())