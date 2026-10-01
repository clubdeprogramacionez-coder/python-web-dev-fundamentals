"""Configuración central para seguridad y conexión.

En un proyecto real aquí se define la configuración de JWT,
secretos y otros parámetros de seguridad.
"""

CONFIGURACION = {
    "secret_key": "cambiar-este-secreto",
    "algorithm": "HS256",
    "token_expire_minutes": 30,
}
