class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(Config):
    # placeholder until production database is created
    # "mariadb+mariadbconnector://<username>:<password>@<host>:<port>/<dbname>"
    SQLALCHEMY_DATABASE_URI = ""

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "mariadb+mariadbconnector:///:memory:"

class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    BCRYPT_LOG_ROUNDS = 4
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = "mariadb+mariadbconnector:///:memory:"