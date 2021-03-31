from credentials import password
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
import pandas as pd

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
        # print(database_exists(engine.url))

def df2postgres(engine, df):
    con = engine.connect()
    df.to_sql(name='schematableseg2', con=con, if_exists='replace', index=True, chunksize=10)

    return con

db = MyDB()
db.create_new_db("ufcDatabaseseg2")
df = pd.read_csv("Resources/data_preprocessed.csv")
con = df2postgres(db.engine, df)
retrievedata = con.execute("select * from schematableseg2 limit 5")
print(retrievedata.fetchall())