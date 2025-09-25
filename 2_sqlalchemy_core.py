from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from dotenv import load_dotenv
import os

load_dotenv()

engine = create_engine(f"postgresql+psycopg2://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_USER')}@localhost:5432/tutorialdatabase", echo=True)

meta = MetaData()

people = Table(
    'people',
    meta,
    Column('id', Integer, primary_key=True),
    Column('name', String, nullable=False),
    Column('age', Integer, nullable=False),
)

meta.create_all(engine)

conn = engine.connect()
insert_statement = people.insert().values(name='Mike', age=30)
result = conn.execute(insert_statement)
conn.commit()