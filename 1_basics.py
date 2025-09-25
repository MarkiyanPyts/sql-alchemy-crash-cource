from sqlalchemy import create_engine, text

engine = create_engine("sqlite:///mydatabase.db", echo=True)

conn = engine.connect()

conn.execute(text("CREATE TABLE IF NOT EXISTS people (name str, age int)"))

conn.commit()

from sqlalchemy.orm import Session

session = Session(engine)

insert_sql_query = text('INSERT INTO people (name, age) VALUES ("Mike", 30);')

session.execute(insert_sql_query)
session.commit()