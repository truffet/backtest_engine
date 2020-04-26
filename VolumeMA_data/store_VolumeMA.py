import mysql.connector
from sqlalchemy import create_engine

def store_VolumeMA(name, df):
	engine = create_engine('mysql+mysqlconnector://root:bodyboard@localhost/kraken_spot_btcusd')
	df.to_sql(con=engine, name=name, if_exists='replace', index=False, chunksize=10000)