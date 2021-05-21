from sqlalchemy import create_engine
from model.base import Base
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///cheykhana')
engine.connect()
conn = engine.connect()

Base.metadata.create_all(engine, checkfirst=True)

Session = sessionmaker(bind=engine)
session = Session()

print("Bog'landi")