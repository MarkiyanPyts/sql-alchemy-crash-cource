from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Float, ForeignKey, func
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

things = Table(
    'things',
    meta,
    Column('id', Integer, primary_key=True),
    Column('description', String, nullable=False),
    Column('value', Float, nullable=False),
    Column('owner', Integer, ForeignKey('people.id'))
)

meta.create_all(engine)

conn = engine.connect()
ground_by_statement = things.select().with_only_columns(things.c.owner, func.sum(things.c.value)).group_by(things.c.owner).having(func.sum(things.c.value) > 100)
result = conn.execute(ground_by_statement)

for row in result.fetchall():
    print(row)

