from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, func
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from dotenv import load_dotenv
import os
load_dotenv()

engine = create_engine(f"postgresql+psycopg2://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_USER')}@localhost:5432/tutorialdatabase", echo=True)
Base = declarative_base()

class Person(Base):
    __tablename__ = 'people' # Usuallyy plural for table names
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer)

    things = relationship("Thing", back_populates="person")

class Thing(Base):
    __tablename__ = 'things'
    id = Column(Integer, primary_key=True)
    description = Column(String, nullable=False)
    value = Column(Float)
    owner = Column(Integer, ForeignKey('people.id'))

    person = relationship("Person", back_populates="things")

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

new_person = Person(name='Charlie', age=70)
session.add(new_person)
# session.flush()  # Flush to get the new person's ID temporarily without committing

new_thing = Thing(description='Watch', value=199.99, person=new_person)
session.add(new_thing)
session.commit()

print("new person: ")
print(new_person.name)
print("new person things: ")
for thing in new_person.things:
    print(thing.description)

tuples_result = session.query(Person.name, Person.age).all()
for row in tuples_result:
    print(row)

objects_result = session.query(Person).filter(Person.age > 30).all()
print([p.name for p in objects_result])

things_result = session.query(Thing).filter(Thing.value != 100).all()
print([t.description for t in things_result])

update_person_query = session.query(Person).filter(Person.name == 'Charlie').update({'name': 'John'})

aggregate_query = session.query(Thing.owner, func.sum(Thing.value)).group_by(Thing.owner).having(func.sum(Thing.value) > 100)
for row in aggregate_query:
    print(row)

#delete_things_query = session.query(Thing).filter(Thing.description == 'Watch').delete()
session.commit()
session.close()