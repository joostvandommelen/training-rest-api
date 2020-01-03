# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 11:41:59 2019

@author: nldomme8
"""

import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
import os
os.chdir('C:/Users/nldomme8/Documents/Projecten/Flask_training')

item_model_module = __import__('20191209_item_model')

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price', 
            type = float,
            required = True,
            help = 'This field cannot be left blank!'
        )
    parser.add_argument('store_id', 
            type = int,
            required = True,
            help = 'Every item needs a store id.'
        )
    
    @jwt_required() 
    def get(self, name):
        item = item_model_module.ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {'message': 'Item not found'}, 404
    
    
    def post(self, name):
        if item_model_module.ItemModel.find_by_name(name):
            return { 'message' : "An item with name '{}' already exists." .format(name)}, 400
        
        data = Item.parser.parse_args()
        
        item = item_model_module.ItemModel(name, data['price'], data['store_id'])
        
        
        try: 
            item.save_to_db()
        except:
            return {'message': 'An error occured while inserting the item.'}, 500 # internal server error
        
        
        return item.json(), 201
    
    

    
    def delete(self, name):
        item = item_model_module.ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
        
        return {'message': 'Item deleted'}
    
    def put(self, name):
        data = Item.parser.parse_args()
        item = item_model_module.ItemModel.find_by_name(name)

        if item is None:
            item = item_model_module.ItemModel(name, data['price'], data['store_id'])
        else:
            item.price = data['price']
        
        item.save_to_db()
        return item.json()
    

    
class ItemList(Resource):
    def get(self):
        return {'items': [item.json() for item in item_model_module.ItemModel.query.all()]}
    
    
    
    
    
    