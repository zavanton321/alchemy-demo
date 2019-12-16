from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from sqlalchemy_declarative import Base, Person, Address

engine = create_engine("sqlite:///sqlalchemy_example.db")
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()

# query object
query = session.query(Person).all()
for person in query:
    print("{0} -> {1}".format(person.name, person.id))

first_person = session.query(Person).first()
print(first_person.name)

addresses = session.query(Address).filter(Address.person == first_person).all()
for address in addresses:
    print(address.street_name)
