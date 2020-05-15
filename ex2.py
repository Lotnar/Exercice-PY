import math
from typing import Any, Union

Ca = float(input(" Digite o comprimento do cateto adjacente "))
Co = float(input(" Digite o comprimento do cateto oposto "))
print(f"Sendo o cateto oposto {Co}cm² e o adjacente {Ca}cm² O comprimento da Hipotenusa é {math.hypot(Ca,Co):.3}cm²")

#exercicio 18
from math import trunc, sin, cos, tan, pi
A = float(input("Forneça um angulo "))
print(f" O angulo {A} tem como seno {sin(A*(pi/180)):.3}, cosseno {trunc(cos(A*(pi/180)))} e tangente {tan(A*(pi/180)):.3}")

#exercicio 19
import random
A = input("Digite seu nome ")
B = input("Digite seu nome ")
C = input("Digite seu nome ")
D = input("Digite seu nome ")
print(f" Os alunos são {A}, {B}, {C}. {D}")
E = random.randint(1, 4)
if int(E) is 1:
    print(f" O sorteado foi {A}")
if int(E) is 2:
    print(f" O sorteado foi {B}")
if int(E) is 3:
    print(f" O sorteado foi {C}")
if int(E) is 4:
    print(f" O sorteado foi {D}")

#desafio 20
from random import shuffle

A = input("Digite seu nome ")
B = input("Digite seu nome ")
C = input("Digite seu nome ")
D = input("Digite seu nome ")
print(f" Os alunos são {A}, {B}, {C}. {D}")
Lista = [A, B, C, D]
shuffle(Lista)
print("A ordem de apresentação será")
print(f"{Lista}")