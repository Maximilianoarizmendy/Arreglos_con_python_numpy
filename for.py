import os
import time

#ciclo for
inicio = time.time()
for i in range(5):
    print(i)
fin = time.time()
tiempoFinal = fin - inicio
print("Tiempo de ejecución con for:", tiempoFinal)

# Pausa de 5 segundos para observar el resultado
time.sleep(5)

# Limpiar consola (Windows o Linux/Mac)
os.system("cls")

#ciclo while
inicio = time.time()
contador = 0
while contador < 5:
    print(contador)
    contador += 1
fin = time.time()
tiempoFinal = fin - inicio
print("Tiempo de ejecución con while:", tiempoFinal)

# Pausa de 5 segundos para observar el resultado
time.sleep(5)

# Limpiar consola
os.system("cls")
