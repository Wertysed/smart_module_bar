import os
from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")
DB_NAME = os.environ.get("DB_NAME")
DB_USER = os.environ.get("DB_USER")
DB_PASS = os.environ.get("DB_PASS")

SSH_HOST = os.environ.get("SSH_HOST")
SSH_USER = os.environ.get("SSH_USER")
SSH_PASS = os.environ.get("SSH_PASS")


SECRET_AUTH = os.environ.get("SECRET_AUTH")