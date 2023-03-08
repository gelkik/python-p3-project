from sqlalchemy import create_engine
from sqlalchemy import ForeignKey, Column, DateTime, Integer, String
from sqlalchemy.orm import relationship, backref
# from sqlalchemy.orm import sessionmaker

from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///p3_project.db')

Base = declarative_base()

class Store(Base):
    __tablename__ = 'stores'

    id = Column(Integer(), primary_key = True)
    store_name = Column(String())
    quantity = Column(Integer())
    customer_id = Column(Integer(), ForeignKey('customers.id'))
    parts_id = Column(Integer(), ForeignKey('parts.id'))

    customer = relationship('Customer', back_populates='stores')
    part = relationship('Part', back_populates='stores')


    def __repr__(self):
        return f"Store {self.id}: " \
            + f"{self.store_name}, " \
            + f"{self.quantity}, " 

class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer(), primary_key = True)
    name = Column(String())
    budget = Column(Integer())
    preference = Column(String())

    store = relationship('Store', backref=backref('customer'))

    def __repr__(self):
        return f"Customer {self.id}: " \
            + f"{self.name}, " \
            + f"Budget: {self.budget}" \
            + f"Preference: {self.preference}"

class Part(Base):
    __tablename__ = 'parts'

    id = Column(Integer(), primary_key = True)
    part_name = Column(String())
    cost = Column(Integer())
    brand = Column(Integer())

    store = relationship('Store', backref=backref('part'))

    def __repr__(self):
        return f"Part {self.id}: " \
            + f"{self.part_name}, " \
            + f"Cost: {self.cost}" \
            + f"Brand: {self.cost}" \
    
    
