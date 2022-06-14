from sqlalchemy import create_engine, MetaData

# import pymysql

engine = create_engine("sqlite:///./blog.db")
meta = MetaData()
conn = engine.connect()
