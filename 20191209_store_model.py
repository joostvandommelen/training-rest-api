# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 13:04:55 2019

@author: nldomme8
"""


import os

os.chdir('C:/Users/nldomme8/Documents/Projecten/Flask_training')
db_module = __import__('20191209_db')


class StoreModel(db_module.db.Model):
    __tablename__ = 'stores'
    
    id = db_module.db.Column(db_module.db.Integer, primary_key = True)
    name = db_module.db.Column(db_module.db.String(80))
    
    items = db_module.db.relationship('ItemModel', lazy = 'dynamic') #not loading at start of script, only by api call
    
    
    def __init__(self, name):
        self.name = name
        
    def json(self):
        return {'name':self.name, 'items': [item.json() for item in self.items.all()]}
    
    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first() # select * from items where name = name LIMIT 1
             
    def save_to_db(self):
        db_module.db.session.add(self)
        db_module.db.session.commit()
             
    def delete_from_db(self):
        db_module.db.session.delete(self)
        db_module.db.session.commit()
        
    