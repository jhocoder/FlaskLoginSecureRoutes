class Config():
    SECRET_KEY = "2564e7a40d937d48e40aa3671bb577ec6456f613c8286ce2949517289f20e894"


class DevelopmentConfig(Config):
    MYSQL_DEBUG = True
    MYSQL_HOST ="127.0.0.1"
    MYSQL_USER="root"
    MYSQL_PASSWORD="1234"
    MYSQL_DB="flask_login"
    
class ProductionConfig(Config):
    MYSQL_DEBUG = False
    MYSQL_HOST ="127.0.0.1"
    MYSQL_USER="root"
    MYSQL_PASSWORD="1234"
    MYSQL_DB="flask_login"
    
    
config = {
        'development': DevelopmentConfig,
        'production': ProductionConfig
}