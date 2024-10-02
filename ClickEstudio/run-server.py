import subprocess
import socket

def is_port_available(port):
    """Verifica si un puerto está disponible."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(('localhost', port)) != 0  # Retorna True si el puerto está libre

def get_valid_port():
    """Solicita un puerto válido al usuario."""
    while True:
        try:
            port = int(input("Ingresa el puerto en el que deseas ejecutar el servidor (por defecto 8000): ") or 8000)
            if 0 <= port <= 65535:  # Verifica que el puerto esté en el rango válido
                return port
            else:
                print("Por favor, ingresa un número de puerto entre 0 y 65535.")
        except ValueError:
            print("Entrada no válida. Asegúrate de ingresar un número entero.")

# Solicitar al usuario un puerto válido
port = get_valid_port()

# Verificar si el puerto está disponible
if is_port_available(port):
    # Ejecutar el servidor de Django en el puerto especificado
    subprocess.run(["python3", "manage.py", "runserver", str(port)])
    print(f"Servidor de Django ejecutándose en el puerto: {port}")
else:
    print(f"El puerto {port} ya está en uso. Por favor, elige otro puerto.")