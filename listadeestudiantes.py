class Estudiante:
    def __init__(self, nombre, carne, carrera, nota_final):
        self.nombre =nombre
        self.carne = carne
        self.carrera = carrera
        self.nota_final = nota_final
    def __str__(self):
        print(f"Nombre: {self.nombre}")
        print(f"Carne: {self.carne}")
        print(f"Carrera: {self.carrera}")
        print(f"Nota final: {self.nota_final}")

