"""
Problema 1:
Implemente un programa que solicite al usuario una fracción, con formato X/Y, donde cada uno de X e Y es un número entero, 
y luego muestra, como un porcentaje redondeado al número entero más cercano, donde se indicará la cantidad de combustible 
en el tanque. Se debe tener en cuenta los siguientes casos:
- Colocar E en caso X/Y sea menor a 1% del total
- Colocar F en caso X/Y sea mayor a 99%.
- En otro caso, devolver el valor en porcentaje %
También debe tomar en cuenta los siguientes casos:
- X y Y deben ser números enteros
- X debe ser menor o igual a Y, y Y != 0
De no cumplirse estos casos, se debe volver a preguntar al usuario. Asegúrese de detectar cualquier excepción como 
ValueError o ZeroDivisionError.
"""

def main():
    while True:
        fraccion = input("Ingrese una fracción (formato X/Y): ").strip()
        
        try:
            # Verificar si hay exactamente una barra en la fracción ingresada
            if fraccion.count('/') != 1:
                raise ValueError("Formato incorrecto. Debe ser X/Y.")
            
            x_str, y_str = fraccion.split('/')
            x = int(x_str.strip())
            y = int(y_str.strip())
            
            if y == 0:
                raise ZeroDivisionError("El denominador no puede ser cero.")
            
            if x > y:
                raise ValueError("X debe ser menor o igual a Y.")
            
            # Calcular porcentaje
            porcentaje = x / y
            
            if porcentaje < 0.01:
                print("E")
            elif porcentaje > 0.99:
                print("F")
            else:
                print(f"{round(porcentaje * 100)}%")
            
            break  # Salir del bucle si todo está correcto
        
        except ValueError as e:
            if "invalid literal for int()" in str(e):
                print("Error: X e Y deben ser números enteros.")
            else:
                print(f"Error: {e}")
            print("Vuelva a intentar.\n")
        except ZeroDivisionError as e:
            print(f"Error: {e}")
            print("Vuelva a intentar.\n")

if __name__ == "__main__":
    main()