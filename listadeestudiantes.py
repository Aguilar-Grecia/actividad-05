class Estudiante:
    def __init__(self, nombre, carne, carrera, nota_final):
        self.nombre =nombre
        self.carne = carne
        self.carrera = carrera
        self.nota_final = nota_final
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
                    print("La nota tiene que estar entre 0 y 100.")
            except ValueError:
                print("Ingreso un numero fuera del rango mencionado. Por favor, intentelo de nuevo.")
        nuevo_estudiante = Estudiante(nombre, carne, carrera, nota_final)
        self.estudiante.append(nuevo_estudiante)
        print(f"Estudiante {nombre} con carné {carne}, ha sigo registrado exitosamente. ")
    def mostrar_estudiantes(self):
        if not self.estudiante:
            print("No hay ningun estudiante registrado")
            return
        print("---Listado de estudiantes registrados---")
        for estudiante in self.estudiante:
            print(f"Nombre: {estudiante.nombre}")
            print(f"Carne: {estudiante.carne}")
            print(f"Carrera: {estudiante.carrera}")
            print(f"Nota final: {estudiante.nota_final}")
    def buscar_estudiante_por_su_carne(self):
        if not self.estudiante:
            print("No hay ningun estudiante registrado para buscar")
            return
        print("---Buscar etudiante por su carne---")
        carne_buscar = input("Ingrese el carne del estudiante que desea bucar: ")


