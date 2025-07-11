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
    def __init__(self):
        self.estudiante = []
    def registrar_estudiante(self):
        print("Registrar nuevo estudiante")
        nombre = input("Ingrese el carne del nuevo estudiante: ")
        carrera = input("Ingrese el carrera del nuevo estudiante: ")
        while True:
            try:
                nota_final = float(input("Ingrese la nota final del estudiante: "))
                if 0 <= nota_final <= 100:
                    break
                else:

