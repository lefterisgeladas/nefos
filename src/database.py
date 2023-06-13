from sqlalchemy import create_engine
from sqlalchemy import text
from sqlalchemy import exc
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
import time

SQLALCHEMY_DATABASE_URL = os.environ.get('DATABASE_URL')

#SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root@localhost:3306/myfastdb"

#ektelei tin sundesi me tin vasi
def get_engine():
    engine = create_engine(SQLALCHEMY_DATABASE_URL)
    return engine

#elegxw na dw pote i vasi einai diathesimi (mexri na einai diathesimo to container)
while True:
    try:
        engine = get_engine()
        with engine.connect() as conn:
            #elegxw an sundethike ektelwntas ena aplo erwtima (SELECT 1)
            sqlt = text('SELECT 1')
            result = conn.execute(sqlt)
            break
    except exc.OperationalError:
        print('MySQL server not available, retrying in 5 seconds...')
        time.sleep(5)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


