"""
Problema 9:
FIGlet, llamado así por las cartas de Frank, Ian y Glen, es un programa de principios de la
década de 1990 para hacer letras grandes a partir de texto ordinario, una forma de arte ASCII:
- En la siguiente web puede ver una lista de fuentes admitidas por FIGlet
figlet.org/examples.html
- Desde entonces, FIGlet ha sido portado a Python como un módulo llamado pyfiglet.
Cree un programa el cual cumpla con las siguientes especificaciones:
- Solicite al usuario el nombre de una fuente a utilizar. En caso no sé ingrese ninguna
fuente, su programa deberá seleccionar de forma aleatoria la fuente a utilizar.
- Solicite al usuario un texto.
- Finalmente, su programa deberá imprimir el texto solicitado usando la fuente
apropiada.
"""

from pyfiglet import Figlet
import random

def mostrar_fuentes_disponibles():
    """Muestra algunas fuentes disponibles como ejemplo"""
    figlet = Figlet()
    fuentes = figlet.getFonts()
    
    print("\n📝 Algunas fuentes disponibles:")
    muestras = random.sample(fuentes, min(10, len(fuentes)))
    for i, fuente in enumerate(muestras, 1):
        print(f"   {i}. {fuente}")
    print(f"   ... y {len(fuentes) - 10} más" if len(fuentes) > 10 else "")
    
    return fuentes

def main():
    print("="*50)
    print("           PROBLEMA 9 - FIGlet (Arte ASCII)")
    print("="*50)
    
    # Crear objeto Figlet
    figlet = Figlet()
    
    try:
        # Mostrar algunas fuentes disponibles
        fuentes_disponibles = mostrar_fuentes_disponibles()
        
        # Solicitar fuente al usuario
        fuente_seleccionada = input("\n🎨 Ingrese el nombre de la fuente (o Enter para aleatoria): ").strip()
        
        if not fuente_seleccionada:
            # Selección aleatoria
            fuente_seleccionada = random.choice(fuentes_disponibles)
            print(f"🎲 Fuente seleccionada aleatoriamente: {fuente_seleccionada}")
        else:
            # Validar que la fuente existe
            if fuente_seleccionada not in fuentes_disponibles:
                print(f"❌ Fuente '{fuente_seleccionada}' no encontrada.")
                print("🔍 Use una fuente de la lista o Enter para aleatoria.")
                return
        
        # Configurar la fuente
        figlet.setFont(font=fuente_seleccionada)
        
        # Solicitar texto al usuario
        texto = input("\n📝 Ingrese el texto a mostrar: ").strip()
        
        if not texto:
            print("❌ Debe ingresar algún texto.")
            return
        
        # Mostrar resultado
        print("\n" + "="*50)
        print("🎨 RESULTADO:")
        print("="*50)
        print(figlet.renderText(texto))
        print(f"🔤 Texto: '{texto}'")
        print(f"📛 Fuente: {fuente_seleccionada}")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        print("💡 Asegúrate de tener pyfiglet instalado: pip install pyfiglet")

if __name__ == "__main__":
    main()