"""
Resolver estos problemas en un único script .py. Agregar control de errores según sea
conveniente. Podría realizar un programa menú que permita realizar todos los puntos
mencionados.
"""
import sys

# ========== CLASES (Problema 4) ==========
class RECTANGULO:
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho
    
    def calcular_area(self):
        return self.largo * self.ancho

class CUADRADO(RECTANGULO):
    def __init__(self, lado):
        super().__init__(largo=lado, ancho=lado)

# ========== LISTA GLOBAL DE ALUMNOS ==========
lista_alumnos = []

# ========== FUNCIONES ==========

# ========== (Problema 3) ==========
def cargar_alumnos():
    """Problema 3: Cargar n alumnos con 3 notas cada uno"""
    global lista_alumnos
    try:
        n = int(input("¿Cuántos alumnos desea cargar? "))
        if n <= 0:
            print("Debe ingresar un número mayor a 0.")
            return
        
        lista_alumnos.clear()
        
        for i in range(n):
            print(f"\nAlumno {i+1}:")
            nombre = input("Nombre completo: ").strip()
            if not nombre:
                print("El nombre no puede estar vacío. Se omitirá este alumno.")
                continue
            
            notas = []
            for j in range(3):
                while True:
                    try:
                        nota = float(input(f"Nota {j+1} (0-10): "))
                        if 0 <= nota <= 10:
                            notas.append(nota)
                            break
                        else:
                            print("La nota debe estar entre 0 y 10.")
                    except ValueError:
                        print("Ingrese un número válido.")
            
            alumno = {
                "nombre": nombre,
                "notas": notas,
                "promedio": sum(notas) / len(notas)
            }
            lista_alumnos.append(alumno)
        
        print(f"\n✅ Se cargaron {len(lista_alumnos)} alumnos correctamente.")
    
    except ValueError:
        print("Error: Ingrese un número entero válido.")

def mostrar_alumnos():
    """Mostrar listado de alumnos cargados"""
    if not lista_alumnos:
        print("No hay alumnos cargados. Use la opción 1 primero.")
        return
    
    print("\n--- LISTADO DE ALUMNOS ---")
    for i, alumno in enumerate(lista_alumnos, 1):
        print(f"{i}. {alumno['nombre']} - Notas: {alumno['notas']} - Promedio: {alumno['promedio']:.2f}")

# ========== (Problema 4) ==========
def rectangulo_y_cuadrado():
    """Problema 4: Demostrar clases RECTANGULO y CUADRADO"""
    try:
        print("\n--- RECTÁNGULO ---")
        largo = float(input("Largo del rectángulo: "))
        ancho = float(input("Ancho del rectángulo: "))
        rect = RECTANGULO(largo, ancho)
        print(f"Área del rectángulo: {rect.calcular_area()}")
        
        print("\n--- CUADRADO ---")
        lado = float(input("Lado del cuadrado: "))
        cuadrado = CUADRADO(lado)
        print(f"Área del cuadrado: {cuadrado.calcular_area()}")
    
    except ValueError:
        print("Error: Ingrese valores numéricos válidos.")

# ========== (Problema 5) ==========
def aprobados_desaprobados():
    """Problema 5: Contar aprobados y desaprobados"""
    if not lista_alumnos:
        print("No hay alumnos cargados. Use la opción 1 primero.")
        return
    
    aprobados = 0
    desaprobados = 0
    
    for alumno in lista_alumnos:
        if alumno['promedio'] >= 4:
            aprobados += 1
        else:
            desaprobados += 1
    
    print(f"\n--- RESULTADOS ---")
    print(f"Aprobados: {aprobados}")
    print(f"Desaprobados: {desaprobados}")

# ========== (Problema 6) ==========
def promedio_curso():
    """Problema 6: Promedio de nota del curso total"""
    if not lista_alumnos:
        print("No hay alumnos cargados. Use la opción 1 primero.")
        return
    
    total_promedios = sum(alumno['promedio'] for alumno in lista_alumnos)
    promedio_curso = total_promedios / len(lista_alumnos)
    
    print(f"\n--- PROMEDIO DEL CURSO ---")
    print(f"Promedio general: {promedio_curso:.2f}")

# ========== (Problema 7.1) ==========
def mejor_peor_promedio():
    """Problema 7: Mejor y peor promedio"""
    if not lista_alumnos:
        print("No hay alumnos cargados. Use la opción 1 primero.")
        return
    
    mejor_alumno = max(lista_alumnos, key=lambda a: a['promedio'])
    peor_alumno = min(lista_alumnos, key=lambda a: a['promedio'])
    
    print(f"\n--- MEJOR Y PEOR PROMEDIO ---")
    print(f"Mejor promedio: {mejor_alumno['nombre']} - {mejor_alumno['promedio']:.2f}")
    print(f"Peor promedio: {peor_alumno['nombre']} - {peor_alumno['promedio']:.2f}")

# ========== (Problema 7.2) ==========
def buscar_alumno():
    """Problema 7 bis: Buscar alumno por nombre (completo o parcial)"""
    if not lista_alumnos:
        print("No hay alumnos cargados. Use la opción 1 primero.")
        return
    
    nombre_buscar = input("Ingrese nombre (completo o parcial): ").strip().lower()
    resultados = []
    
    for alumno in lista_alumnos:
        if nombre_buscar in alumno['nombre'].lower():
            resultados.append(alumno)
    
    if resultados:
        print(f"\n--- RESULTADOS DE BÚSQUEDA ('{nombre_buscar}') ---")
        for alumno in resultados:
            print(f"Nombre: {alumno['nombre']} - Notas: {alumno['notas']} - Promedio: {alumno['promedio']:.2f}")
    else:
        print("No se encontraron alumnos con ese nombre.")

# ========== MENÚ PRINCIPAL ==========
def main():
    while True:
        print("\n" + "="*50)
        print("           MENÚ PRINCIPAL - FUNCIONES")
        print("="*50)
        print("1. Cargar alumnos")
        print("2. Mostrar listado de alumnos")
        print("3. Rectángulo y Cuadrado")
        print("4. Aprobados y desaprobados")
        print("5. Promedio del curso")
        print("6. Mejor y peor promedio")
        print("7. Buscar alumno por nombre")
        print("8. Salir")
        print("="*50)
        
        opcion = input("Seleccione una opción (1-8): ").strip()
        
        if opcion == "1":
            cargar_alumnos()
        elif opcion == "2":
            mostrar_alumnos()
        elif opcion == "3":
            rectangulo_y_cuadrado()
        elif opcion == "4":
            aprobados_desaprobados()
        elif opcion == "5":
            promedio_curso()
        elif opcion == "6":
            mejor_peor_promedio()
        elif opcion == "7":
            buscar_alumno()
        elif opcion == "8":
            print("¡Hasta luego!")
            sys.exit()
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()