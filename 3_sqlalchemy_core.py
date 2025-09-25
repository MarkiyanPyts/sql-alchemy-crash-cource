from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Float, ForeignKey
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
    Column('owner_id', Integer, ForeignKey('people.id'))
)

meta.create_all(engine)

conn = engine.connect()
insert_people = people.insert().values(
    [
        {'name': 'Alice', 'age': 28},
        {'name': 'Bob', 'age': 35},
        {'name': 'Charlie', 'age': 25},
        {'name': 'Diana', 'age': 32},
        {'name': 'Ethan', 'age': 45}
    ]
)

insert_things = things.insert().values(
    [
        {'description': 'Laptop', 'value': 1200.00, 'owner_id': 1},
        {'description': 'Smartphone', 'value': 800.00, 'owner_id': 7},
        {'description': 'Bicycle', 'value': 300.00, 'owner_id': 8},
        {'description': 'Guitar', 'value': 500.00, 'owner_id': 9},
        {'description': 'Camera', 'value': 700.00, 'owner_id': 11}
    ]
)


conn.execute(insert_people)
conn.execute(insert_things)
conn.commit()