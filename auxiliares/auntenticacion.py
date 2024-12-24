from werkzeug.security import generate_password_hash, check_password_hash

def hash_password(password):
    # """Genera un hash seguro para la contraseña proporcionada."""
    return generate_password_hash(password)

def verify_password(stored_password, provided_password):
    # """Verifica si la contraseña proporcionada coincide con la almacenada."""
    return check_password_hash(stored_password, provided_password)