import os

def eliminar_carpetas_vacias(ruta):
    # Revisar todas las carpetas dentro de la ruta proporcionada
    for carpeta in os.listdir(ruta):
        ruta_carpeta = os.path.join(ruta, carpeta)
        
        # Verificar si es una carpeta
        if os.path.isdir(ruta_carpeta):
            # Comprobar si la carpeta está vacía
            if not os.listdir(ruta_carpeta):
                # Si está vacía, eliminarla
                os.rmdir(ruta_carpeta)
                print(f"Carpeta vacía eliminada: {ruta_carpeta}")
            else:
                # Si contiene archivos, informar
                print(f"Carpeta con archivos: {ruta_carpeta}")

# Ruta de la carpeta a revisar
ruta_carpeta_principal = "C:/ruta/a/tu/carpeta"  # Cambia esta ruta según tu sistema

# Llamada a la función
eliminar_carpetas_vacias(ruta_carpeta_principal)