# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 12:00:17 2019

@author: nldomme8
"""
import sqlite3
import os

os.chdir('C:/Users/nldomme8/Documents/Projecten/Flask_training')
db_module = __import__('20191209_db')

class UserModel(db_module.db.Model):
    __tablename__ = 'users'
    
    id = db_module.db.Column(db_module.db.Integer, primary_key = True)
    username = db_module.db.Column(db_module.db.String(80))
    password = db_module.db.Column(db_module.db.String(80))
    
    def __init__(self, username, password):
        self.username = username
        self.password = password
        
    def save_to_db(self):
        db_module.db.session.add(self)
        db_module.db.session.commit()
    
    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()
        
    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()