from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import DB_HOST, DB_NAME, DB_PASS, DB_PORT, DB_USER, SSH_HOST, SSH_PASS, SSH_USER
# from sshtunnel import SSHTunnelForwarder
# server = SSHTunnelForwarder(
#     (SSH_HOST, 22),
#     ssh_username=SSH_USER,
#     ssh_password=SSH_PASS,
#     remote_bind_address=(DB_HOST, 5432)
#     )
#
# server.start()
SQLALCHEMY_DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
