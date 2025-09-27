"""
Problema 8:
Empleando la API de SUNAT vista en clase, debemos obtener los diferentes valores para el tipo
de cambio durante el año 2025 hasta donde se tenga información. Una vez realizado ello
calcular:
- Obtener las fechas donde el valor de compra del dólar sea el mínimo.
- Obtener las fechas donde el valor de venta del dólar sea máximo.
- Obtener aquellas fechas donde el valor de la diferencia de compraventa sea máxima.
"""

import requests
import time

def obtener_tipo_cambio_2025_inteligente():
    """
    Versión INTELIGENTE - Descubre automáticamente hasta qué mes hay datos
    con tiempos de espera optimizados
    """
    print("🔍 Obteniendo datos de tipo de cambio 2025 (versión inteligente)...")
    
    todos_datos = []
    mes = 1
    meses_sin_datos_consecutivos = 0  # Contador para detectar fin de datos
    
    while mes <= 12 and meses_sin_datos_consecutivos < 2:  # Parar después de 2 meses sin datos
        try:
            url = f"https://api.apis.net.pe/v1/tipo-cambio-sunat?month={mes}&year=2025"
            print(f"📅 Consultando mes {mes}/2025...")
            
            response = requests.get(url, timeout=10)
            
            # Manejo optimizado del error 429
            if response.status_code == 429:
                print("⏳ Límite de API. Esperando 10 segundos...")
                time.sleep(10)  # Solo 10 segundos de espera
                
                # Un solo reintento
                response = requests.get(url, timeout=10)
                if response.status_code == 429:
                    print("🚫 Límite persistente. Saltando al siguiente mes...")
                    mes += 1
                    continue
            
            response.raise_for_status()
            
            datos_mes = response.json()
            
            if datos_mes:
                todos_datos.extend(datos_mes)
                print(f"✅ Mes {mes}: {len(datos_mes)} registros")
                meses_sin_datos_consecutivos = 0  # Resetear contador
            else:
                print(f"📭 No hay datos para mes {mes}.")
                meses_sin_datos_consecutivos += 1
                if meses_sin_datos_consecutivos >= 2:
                    print("💡 Detectados 2 meses consecutivos sin datos. Terminando búsqueda.")
                    break
            
            # Pausa mínima entre consultas exitosas
            time.sleep(0.5)
            mes += 1
            
        except requests.exceptions.RequestException as e:
            print(f"❌ Error en mes {mes}: {e}")
            # En caso de error, intentar con el siguiente mes
            mes += 1
            continue
    
    return todos_datos

def analizar_datos(datos):
    """Analiza los datos y calcula los resultados solicitados"""
    if not datos:
        print("❌ No se obtuvieron datos para analizar.")
        return
    
    print(f"\n📊 Total de registros obtenidos: {len(datos)}")
    
    if len(datos) == 0:
        return
    
    # 1. Encontrar MÍNIMO valor de COMPRA
    min_compra = min(datos, key=lambda x: x['compra'])
    valor_min_compra = min_compra['compra']
    
    fechas_min_compra = [
        registro['fecha'] for registro in datos 
        if registro['compra'] == valor_min_compra
    ]
    
    # 2. Encontrar MÁXIMO valor de VENTA
    max_venta = max(datos, key=lambda x: x['venta'])
    valor_max_venta = max_venta['venta']
    
    fechas_max_venta = [
        registro['fecha'] for registro in datos 
        if registro['venta'] == valor_max_venta
    ]
    
    # 3. Encontrar MÁXIMA DIFERENCIA (venta - compra)
    for registro in datos:
        registro['diferencia'] = registro['venta'] - registro['compra']
    
    max_diferencia = max(datos, key=lambda x: x['diferencia'])
    valor_max_diferencia = max_diferencia['diferencia']
    
    fechas_max_diferencia = [
        registro['fecha'] for registro in datos 
        if registro['diferencia'] == valor_max_diferencia
    ]
    
    # Mostrar resultados
    print("\n" + "="*60)
    print("📈 RESULTADOS DEL ANÁLISIS")
    print("="*60)
    
    print(f"\n💰 VALOR MÍNIMO DE COMPRA: S/ {valor_min_compra:.3f}")
    print("📅 Fechas con este valor:")
    for fecha in fechas_min_compra[:5]:  # Mostrar máximo 5 fechas
        print(f"   - {fecha}")
    if len(fechas_min_compra) > 5:
        print(f"   ... y {len(fechas_min_compra) - 5} fechas más")
    
    print(f"\n💵 VALOR MÁXIMO DE VENTA: S/ {valor_max_venta:.3f}")
    print("📅 Fechas con este valor:")
    for fecha in fechas_max_venta[:5]:
        print(f"   - {fecha}")
    if len(fechas_max_venta) > 5:
        print(f"   ... y {len(fechas_max_venta) - 5} fechas más")
    
    print(f"\n📊 MÁXIMA DIFERENCIA (Venta - Compra): S/ {valor_max_diferencia:.3f}")
    print("📅 Fechas con esta diferencia:")
    for fecha in fechas_max_diferencia[:5]:
        print(f"   - {fecha}")
    if len(fechas_max_diferencia) > 5:
        print(f"   ... y {len(fechas_max_diferencia) - 5} fechas más")
    
    # Estadísticas adicionales
    primer_registro = datos[0]['fecha']
    ultimo_registro = datos[-1]['fecha']
    print(f"\n📅 Rango de fechas: {primer_registro} a {ultimo_registro}")
    print(f"📈 Promedio compra: S/ {sum(r['compra'] for r in datos)/len(datos):.3f}")
    print(f"📈 Promedio venta: S/ {sum(r['venta'] for r in datos)/len(datos):.3f}")

def main():
    """Función principal"""
    print("="*60)
    print("             PROBLEMA 8 - API SUNAT (2025)")
    print("="*60)
    
    try:
        # Obtener datos de forma inteligente
        datos = obtener_tipo_cambio_2025_inteligente()
        
        if datos:
            # Analizar datos
            analizar_datos(datos)
        else:
            print("❌ No se pudieron obtener datos.")
    
    except KeyboardInterrupt:
        print("\n⏹️ Programa interrumpido por el usuario.")
    except Exception as e:
        print(f"❌ Error inesperado: {e}")

if __name__ == "__main__":
    main()