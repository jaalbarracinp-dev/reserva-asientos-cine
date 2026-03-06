# Crear matriz 3x4 con todos los asientos libres
asientos = [[0 for j in range(4)] for i in range(3)]

# Pedir fila y columna
f = int(input("Ingrese fila (0 a 2): "))
c = int(input("Ingrese columna (0 a 3): "))

# Reservar asiento
asientos[f][c] = 1

# Mostrar estado de la sala
print("\nEstado de la sala:")

for i in range(3):
    for j in range(4):
        print(asientos[i][j], end=" ")
    print()