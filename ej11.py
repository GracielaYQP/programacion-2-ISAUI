# Realizar un programa que sume dos matrices de 2x2 y muestre el resultado
from random import random

import random
mat1=[]
mat2=[]
matsuma=[]
Msj=""
for i in range(0,2):
    mat1.append([0]*2)
    mat2.append([0]*2)
    matsuma.append([0]*2)
for i in range(0,2):
    for j in range(0,2):
        num1 = random.randint(0,10)
        mat1[i][j]=num1
for i in range(0,2):
    for j in range(0,2):        
        Msj = Msj + " " + str(mat1 [i][j])
    Msj = Msj + "\n"
# Msj=""
# for i in range(0,2):
#     for j in range(0,2):    
#         num2 = random.randint(0,10)
#         mat2[i][j]=num2
# for i in range(0,2):
#     for j in range(0,2):       
#         Msj = Msj + " " + str(mat2 [i][j])
#     Msj = Msj + "\n"
# Msj=""
# for i in range(0,2):
#     for j in range(0,2):
#         suma=mat1[i][j]+mat2[i][j]
#         matsuma.append(suma)
# for i in range(0,2):
#     for j in range(0,2):         
#         Msj = Msj + " " + str(matsuma [i][j])
#     Msj = Msj + "\n"

#en este ejercicio esta sin terminar
