import os
import secrets
from dotenv import load_dotenv


# Using python-dotenv to load environment variables if the .env file is present
env_path = ".env"
if os.path.isfile(env_path):
    load_dotenv(dotenv_path=env_path)

# If the .env isn't present, we assume that the variables were
# exported in the CLI as in the lab instructions


class Config(object):
    """Base Config Object"""
    DEBUG = False
    SECRET_KEY = secrets.token_urlsafe(30) or 'Som3$ec5etK*y'
    MAIL_SERVER = os.environ.get('MAIL_SERVER') or 'localhost'
    MAIL_PORT = os.environ.get('MAIL_PORT') or '25'
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')


class DevelopmentConfig(Config):
    """Development Config that extends the Base Config Object"""
    DEVELOPMENT = True
    DEBUG = True


class ProductionConfig(Config):
    """Production Config that extends the Base Config Object"""
    DEBUG = False
