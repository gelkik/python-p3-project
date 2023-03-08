from random import choice as rc
import random
from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Store, Customer, Part

engine = create_engine('sqlite:///p3_project.db')
Session = sessionmaker(bind=engine)
session = Session()
fake = Faker()

part_name = ['CPU', 'Motherboard','RAM','GPU', 'Case','Monitor','Power Supply','HDD', 
               'Mouse','Keyboard', 'Cooling Fans','SDD']

brand = {'Case':{'Asus','Dell','MSI','ASRock','Razer'},
          'Motherboard':{'ASRock','Asus','MSI','Intel','Acer'},
          'CPU':{'AMD','Intel','Qualcomm','IBM','Nvidia'},
          'HDD':{'Toshiba','Samsung','Toshiba','Sony','LG'},
          'SDD':{'Toshiba','Samsung','Toshiba','Sony','LG'},
          'Cooling Fans':{'Corsair','Samsung','Toshiba','Sony','LG'},
          'Monitor':{'Alienwarew','Samsung','Dell','Sony','LG'},
          'GPU':{'Asus','Nvidia','AMD','Biostar','Intel'},
          'Keyboard':{'Amkette','HyperX','Razer','Lenovo','Dell'},
          'Mouse':{'Corsair','Alienware','Razer','HyperX','Sony'},
          'Power Supply':{'Corsair','Foxconn','Razer','Thermaltake','Razer'},
          'RAM':{'Lenovo','Asus','IBM','Toshiba','HyperX'},
        }
# https://en.wikipedia.org/wiki/List_of_computer_hardware_manufacturers

stores = ['Amazon','Best Buy','NewEgg','B&H','Micro Center','GameStop']

def delete_records():
    session.query(Store).delete()
    session.query(Customer).delete()
    session.query(Part).delete()
    session.commit()

# def create_records():
#     stores = [Store() for i in range(100)]
#     customers = [Customer() for i in range(1000)]
#     parts = [Part() for i in range(500)]
#     session.add_all(stores + customers + parts)
#     session.commit()
#     return stores, customers, parts

def create_records():
    for i in range(50):
        customers = Customer(
                name=f"{fake.first_name()} {fake.last_name()}",
                budget=f"${random.randint(100, 2500)}",
                preference=random.choice(part_name),
            )
    for i in range(50):
        stores = Store(
                store_name=random.choice(stores),
                quantity=[random.randint(0,10)],
            )
    for i in range(50):
        parts = Part(
                part_name=random.choice(part_name),
                cost=f"${random.randint(100, 1000) if part_name in part_name[:7] else random.randint(20,150)}",
                brand=random.choice(brand),
            )
    session.add_all(customers)
    session.commit()
    return customers

if __name__ == '__main__':
    delete_records()
    create_records()

    