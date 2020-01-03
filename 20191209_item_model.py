# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 13:04:55 2019

@author: nldomme8
"""


import os

os.chdir('C:/Users/nldomme8/Documents/Projecten/Flask_training')
db_module = __import__('20191209_db')


class ItemModel(db_module.db.Model):
    __tablename__ = 'items'
    
    id = db_module.db.Column(db_module.db.Integer, primary_key = True)
    name = db_module.db.Column(db_module.db.String(80))
    price = db_module.db.Column(db_module.db.Float(precision=2))
    
    store_id = db_module.db.Column(db_module.db.Integer, db_module.db.ForeignKey('stores.id'))
    store = db_module.db.relationship('StoreModel')
    
    
    def __init__(self, name, price, store_id):
        self.name = name
        self.price = price 
        self.store_id = store_id
        
    def json(self):
        return {'name':self.name, 'price':self.price}
    
    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first() # select * from items where name = name LIMIT 1
             
    def save_to_db(self):
        db_module.db.session.add(self)
        db_module.db.session.commit()
             
    def delete_from_db(self):
        db_module.db.session.delete(self)
        db_module.db.session.commit()
        
    