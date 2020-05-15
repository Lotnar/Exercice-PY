# Estudo dos tipos primitivos e type que indica classe
x = float(input("digite um numero:"))
print(x)
print(type(x))
#Bool
x = bool(input("digite um numero:"))
print(x)
print(type(x))

# Desafio1

x = input("Digite")
print("O tipo primitivo:", type(x))
print("É alfanumerico?", x.isalnum())
print("É alfabetico?", x.isalpha())
print("É um numero?", x.isnumeric())
print("É maisculo?", x.isupper())
print("É decimal?", x.isdecimal())
print("É um espaço?", x.isspace())
print("É um digito?", x.isdigit())
print("Esta capitalizada?", x.istitle())
