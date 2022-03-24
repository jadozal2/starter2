import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    SQL_SERVER = os.environ.get('SQL_SERVER') or 'sqlserver1313.database.windows.net' # '[SQL_SERVER_GOES_HERE]'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'mydatabase' #'[SQL_DATABASE_GOES_HERE]'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'jadozal2' #'[SQL_USER_NAME_GOES_HERE]'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or 'Welcome1313' #'[SQL_PASSWORD_GOES_HERE]'
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE + '?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'storageaccount1234' #'[BLOB_ACCOUNT_GOES_HERE]'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or 'F6HDtA1J2C9NcbcZkQITU9SoHG6OGzMO2Kc8prUZGbvdyYjT7YoEl6/hUuI+RoX4e/CyiACVK45K+AStRN7ypA==' #'[BLOB_STORAGE_KEY_GOES_HERE]'
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'images' #'[BLOB_CONTAINER_GOES_HERE]'
