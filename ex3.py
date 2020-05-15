#exercicio 22
x = str(input("Digite seu nome "))
print(x.upper())
print(x.lower())
print(len(x) - x.count(' ') )
D= x.split()
print(len(D[0]))

#exercicio 24
x=str(input("Digite o nome da cidade "))
print(x.find("Santo"))

#Manipulando Texto
frase= "    Curso de programação   "
print(frase[7:16])
print(frase[:19])
print(frase[7:])
print(frase[7:27:2]) # esse :2 indica pular de dois em dois
print(frase[::2])
print("""A melhor fala de ontem sobre o que ocorreu na Câmara"
foi do nosso líder Paulo Ganime: com classe, demonstrou por que temos 
de destinar o dinheiro do Fundão para o combate ao coronavírus e cortar na própria carne. Sensacional!!! Assista e compartilhe!!!""")
#
print(len(frase))
print(frase.count("o"))
print(frase.count("o",0,13))
print(frase.find("pro"))
print("Curso" in frase)
print(frase.replace("prog", "Android"))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())
print(frase.strip())
print(frase.rstrip())
print(frase.lstrip())
print(frase.split())
print("-".join(frase))
print(frase.upper().count("O"))
dividido = frase.split()
print(dividido[2])
print(dividido[2][3])