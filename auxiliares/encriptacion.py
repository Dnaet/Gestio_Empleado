from cryptography.fernet import Fernet

# Generar una clave y guardarla en un archivo
def generar_clave():
    clave = Fernet.generate_key()
    with open("clave.key", "wb") as clave_archivo:
        clave_archivo.write(clave)

# Cargar la clave desde un archivo
def cargar_clave():
    return open("clave.key", "rb").read()

# Encriptar un mensaje
def encriptar_mensaje(mensaje):
    clave = cargar_clave()
    f = Fernet(clave)
    mensaje_encriptado = f.encrypt(mensaje.encode())
    return mensaje_encriptado

# Desencriptar un mensaje
def desencriptar_mensaje(mensaje_encriptado):
    clave = cargar_clave()
    f = Fernet(clave)
    mensaje_desencriptado = f.decrypt(mensaje_encriptado).decode()
    return mensaje_desencriptado