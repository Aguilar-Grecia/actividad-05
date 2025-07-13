class Estudiante:
    def __init__(self, nombre, carne, carrera, nota_final):
        self.nombre =nombre
        self.carne = carne
        self.carrera = carrera
        self.nota_final = nota_final
    def mostrar(self):
        print(f"Nombre: {self.nombre}, Carné: {self.carne}, Carrera:{self.carrera} Nota final: {self.nota_final}")
class Sistema:
    def __init__(self):
        self.estudiantes = []
    def registrar_estudiante(self):
        nombre = input("Nombre: ")
        carne = input("Carne: ")
        carrera = input("Carrera: ")
        try:
            nota_final = float(input("Nota final: "))
        except ValueError:
            print("La nota no es valida. Intentelo de nuevo. ")
            return
        estudiante = Estudiante(nombre, carne, carrera, nota_final)
        self.estudiante.append(estudiante)
        print("El estudiante ha registrado correctamente. ")
    def mostrar_todos(self):
        if not self.estudiantes:
            print("No hay ningun estudiante registrado. ")
        else:
            print("Lista de estudiantes:")
            for estudiante in self.estudiantes:
                estudiante.mostrar()
            print()
    def buscar_estudiante_por_su_carne(self):
        carne_buscar = input("Por favor, ingrese el carné del estudiante: ")
        encontrado = False
        for estudiante in self.estudiantes:
            if estudiante.carne == carne_buscar:
                print("Estudiante encontrado: ")
                estudiante.mostrar()
                encontrado = True
                break
        if not encontrado:
            print("El estudiante no ha sido encontrado.")
    def calcular_promedio(self):
        if  not self.estudiantes:
            print("No se han registrado notas, no es posible calcular el promedio.")
        else:
            total = sum(estudiante.nota_final for estudiante in self.estudiantes)
            promedio = total/ len(self.estudaintes)
            print(f"Promedio: {promedio}")
    def main(self):
        while True:
            print("1. Registrar estudiante.")
            print("2. Mostrar estudiantes.")
            print("3. Buscar estudiante en la lista.")
            print("4. Calcular promedio")
            print("5. Salir")
            opcion = input("Seleccione una opción: ")

