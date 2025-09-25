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
insert_statement = people.insert().values(name='Jane', age=40)
select_statement = people.select().where(people.c.age > 30)
conn.execute(insert_statement)
result = conn.execute(select_statement)
for row in result.fetchall():
    print(row)

update_statement = people.update().where(people.c.name == 'Jane').values(age=39)
conn.execute(update_statement)

delete_statement = people.delete().where(people.c.name == 'Jane')
conn.execute(delete_statement)
conn.commit()