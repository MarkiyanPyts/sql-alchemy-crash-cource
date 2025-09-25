from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

engine = create_engine("postgresql+psycopg", echo=True)

meta = MetaData()

people = Table(
    'people',
    meta,
    Column('id', Integer, primary_key=True),
    Column('name', String, nullable=False),
    Column('age', Integer, nullable=False),
)

meta.create_all(engine)
