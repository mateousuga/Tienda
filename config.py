class config:
    SECRET_KEY = "llave-secreta-tienda-libros"

class DevelopmentConfig(config):
    Debug = True

config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}