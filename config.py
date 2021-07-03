class Config(object):
    DEBUG = False
    TESTING = False

    

class ProductionConfig(Config):
    SECRET_KEY = '3izb^ryglj(bvrjb2_y1fZvcnbky#358_l6-nn#i8fkug4mmz!'

    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'