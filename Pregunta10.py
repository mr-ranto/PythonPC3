"""
Problema 10:
Del siguiente URL
https://images.unsplash.com/photo-1546527868-ccb7ee7dfa6a?q=80&w=2070&auto=format
&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D
%3D
Descargue la imagen que más le agrade, según lo revisado en la clase. Posteriormente crear un
programa que permita el almacenamiento de la imagen como un archivo zip. Finalmente cree
un código que permita hacer un unzip al archivo zipeado.
"""

import requests
import zipfile
import os
from io import BytesIO

def descargar_imagen(url, nombre_archivo="imagen_ejemplo.jpg"):
    """
    Descarga una imagen desde una URL y la guarda localmente
    """
    try:
        print(f"📥 Descargando imagen desde: {url}")
        response = requests.get(url, timeout=30)
        response.raise_for_status()  # Verificar que la descarga fue exitosa
        
        # Guardar imagen localmente
        with open(nombre_archivo, 'wb') as archivo:
            archivo.write(response.content)
        
        print(f"✅ Imagen descargada: {nombre_archivo} ({len(response.content)} bytes)")
        return nombre_archivo
        
    except requests.exceptions.RequestException as e:
        print(f"❌ Error al descargar la imagen: {e}")
        return None

def crear_zip(archivo_imagen, nombre_zip="imagen_comprimida.zip"):
    """
    Crea un archivo ZIP que contiene la imagen
    """
    try:
        if not os.path.exists(archivo_imagen):
            print(f"❌ El archivo {archivo_imagen} no existe")
            return False
        
        with zipfile.ZipFile(nombre_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
            zipf.write(archivo_imagen, os.path.basename(archivo_imagen))
        
        print(f"✅ Archivo ZIP creado: {nombre_zip}")
        print(f"📦 Tamaño original: {os.path.getsize(archivo_imagen)} bytes")
        print(f"📦 Tamaño comprimido: {os.path.getsize(nombre_zip)} bytes")
        
        # Calcular compresión
        original = os.path.getsize(archivo_imagen)
        comprimido = os.path.getsize(nombre_zip)
        ratio = (1 - comprimido/original) * 100
        print(f"📊 Ratio de compresión: {ratio:.1f}%")
        
        return nombre_zip
        
    except Exception as e:
        print(f"❌ Error al crear ZIP: {e}")
        return False

def extraer_zip(archivo_zip, carpeta_destino="imagen_extraida"):
    """
    Extrae el contenido de un archivo ZIP
    """
    try:
        if not os.path.exists(archivo_zip):
            print(f"❌ El archivo {archivo_zip} no existe")
            return False
        
        # Crear carpeta de destino si no existe
        if not os.path.exists(carpeta_destino):
            os.makedirs(carpeta_destino)
        
        with zipfile.ZipFile(archivo_zip, 'r') as zipf:
            # Mostrar contenido del ZIP
            print(f"📁 Contenido del ZIP:")
            for info in zipf.infolist():
                print(f"   - {info.filename} ({info.file_size} bytes)")
            
            # Extraer todo
            zipf.extractall(carpeta_destino)
        
        print(f"✅ Archivo extraído en: {carpeta_destino}/")
        
        # Listar archivos extraídos
        archivos_extraidos = os.listdir(carpeta_destino)
        print(f"📄 Archivos extraídos: {archivos_extraidos}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error al extraer ZIP: {e}")
        return False

def main():
    print("="*60)
    print("           PROBLEMA 10 - Descarga y Compresión de Imagen")
    print("="*60)
    
    # URL de ejemplo (puedes cambiarla por cualquier imagen de Unsplash)
    url_imagen = "https://images.unsplash.com/photo-1546527868-ccb7ee7dfa6a?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMiA3fDBBMHxwaG90by1wYWdIfHx8fGVufDB8fHx8fA%3D%3D"
    
    try:
        # Paso 1: Descargar imagen
        archivo_imagen = descargar_imagen(url_imagen, "imagen_ejemplo.jpg")
        if not archivo_imagen:
            return
        
        # Paso 2: Crear archivo ZIP
        archivo_zip = crear_zip(archivo_imagen, "imagen_comprimida.zip")
        if not archivo_zip:
            return
        
        # Paso 3: Extraer el ZIP
        print("\n" + "="*40)
        print("🔓 EXTRACCIÓN DEL ARCHIVO ZIP")
        print("="*40)
        extraer_zip(archivo_zip, "imagen_descomprimida")
        
        # Resumen final
        print("\n" + "="*60)
        print("🎉 PROCESO COMPLETADO EXITOSAMENTE")
        print("="*60)
        print("📋 Archivos creados:")
        print(f"   - {archivo_imagen} (imagen original)")
        print(f"   - {archivo_zip} (archivo comprimido)")
        print(f"   - imagen_descomprimida/ (carpeta con imagen extraída)")
        
    except KeyboardInterrupt:
        print("\n⏹️ Programa interrumpido por el usuario.")
    except Exception as e:
        print(f"❌ Error inesperado: {e}")

if __name__ == "__main__":
    main()