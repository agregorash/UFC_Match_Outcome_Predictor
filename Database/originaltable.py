from credentials import password
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
import pandas as pd
import psycopg2

params={"host": "localhost", "user": "postgres", "password": password, "port": 5432}

# useful info for psycopg2:
# https://stackoverflow.com/questions/34484066/create-a-postgres-database-using-python


class MyDB(object):
    def __init__(self):
        self.params = params

    def create_new_db(self, newdb):
        user, host, port = self.params['user'], self.params['host'], self.params['port']
        pw = self.params['password']
        url = 'postgresql://{}:{}@{}:{}/{}'
        url = url.format(user, pw, host, port, newdb)

        self.engine = create_engine(url, client_encoding='utf8')
        if not database_exists(self.engine.url):
            create_database(self.engine.url)

def df2postgres(df):
    url = 'postgresql://{}:{}@{}:{}/{}'
    url = url.format(params["user"], params["password"], params["host"], params["port"], "ufcDatabaseseg2")
    conn = create_engine(url)
    df.to_sql(name='original', con=conn, if_exists='replace', index=False, chunksize=10)

    return conn

df = pd.read_csv("../final_project/Resources/na_filled.csv")
con = df2postgres(df)
