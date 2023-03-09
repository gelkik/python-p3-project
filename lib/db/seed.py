#!/usr/bin/env python3
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

part_names = ['CPU', 'Motherboard','RAM','GPU', 'Case','Monitor','Power Supply','HDD', 
               'Mouse','Keyboard', 'Cooling Fans','SDD']

brands = {'Case':{'Asus','Dell','MSI','ASRock','Razer'},
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
    name = input('Customer name: ')
    budget = int(input('Customer budget: '))
    preference = input(f'Customer preference {part_names}: ')
    customer = Customer(
            name=name,
            budget=budget,
            preference=preference,
        )
    
    store_name = input(f"Store name {stores}: ")
    quantity = int(input('Input quantity: '))
    customer_id = int(input("Enter customer ID: "))
    parts_id = int(input("Enter part ID: "))
    store = Store(
                store_name=store_name,
                quantity=quantity,
                customer_id=customer_id,
                parts_id=parts_id
            )
    part_name = input(f"Part name: {part_names}: ")
    cost = int(input('Part Cost: '))
    brand = input(f"Part brand: {brands}: ")
    part = Part(
            part_name=part_name,
            cost=cost,
            brand=brand,
        )
    session.add_all(customer+store+part)
    session.commit()
    return customer + store + part

if __name__ == '__main__':
    # delete_records()
    create_records()

    