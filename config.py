import os


class Config:

    TESTING = False
    SECRET_KEY = os.environ.get('SECRET_KEY', 'this-is-a-secret-key')

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'postgresql+psycopg2://postgres:postgres123@localhost/nodues')
    SQLALCHEMY_TRACK_MODIFICATIONS = False