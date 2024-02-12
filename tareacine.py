class SalaCine:
    def __init__(self, filas, columnas):
        self.filas = filas
        self.columnas = columnas
        self.asientos_disponibles = [[True] * columnas for _ in range(filas)]
        self.precios = {"Normal": 10, "Económico": 8}

    def mostrar_sala(self):
        print("Estado de la Sala:")
        for i in range(self.filas):
            for j in range(self.columnas):
                if self.asientos_disponibles[i][j]:
                    print("O", end=" ")  # "O" representa un asiento disponible
                else:
                    print("X", end=" ")  # "X" representa un asiento ocupado
            print()

    def elegir_asiento(self, fila, columna, tipo_entrada):
        if 0 <= fila < self.filas and 0 <= columna < self.columnas:
            if self.asientos_disponibles[fila][columna]:
                precio = self.precios.get(tipo_entrada, 0)
                print(f"¡Asiento {fila + 1}-{columna + 1} seleccionado! Precio: ${precio}")
                self.asientos_disponibles[fila][columna] = False
            else:
                print("Lo siento, ese asiento ya está ocupado.")
        else:
            print("Ubicación de asiento no válida.")


sala_cine = SalaCine(filas=5, columnas=10)
sala_cine.mostrar_sala()

fila_elegida = int(input("Ingrese el número de fila deseado: ")) - 1
columna_elegida = int(input("Ingrese el número de columna deseado: ")) - 1
tipo_entrada = input("Seleccione el tipo de entrada (Normal/Económico): ").capitalize()

sala_cine.elegir_asiento(fila_elegida, columna_elegida, tipo_entrada)
sala_cine.mostrar_sala()
