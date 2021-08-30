class Config(object):
    DEBUG = False
    TESTING = False

class ProductionConfig(Config):
    # "mariadb+mariadbconnector://<username>:<password>@<host>:<port>/<dbname>"
    pass

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
    BCRYPT_LOG_ROUNDS = 4
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = "mariadb+mariadbconnector:///:memory:"