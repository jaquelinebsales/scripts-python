altura = float(input("Digite a altura da parede(em metros): "))
largura = float(input("Digite a largura da parede(em metros): "))
área = altura*largura
litrosDeTinta = área/2
print(f"A área é: {área:=.2f}m², e serão utilizados {litrosDeTinta:=.2f} L de tinta.")