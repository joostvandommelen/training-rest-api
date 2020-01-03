# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 10:22:03 2019

@author: nldomme8
"""

from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
import os
os.chdir('C:/Users/nldomme8/Documents/Projecten/Flask_training')

item_model_module = __import__('20191209_item_model')
store_model_module = __import__('20191209_store_model')

class Store(Resource):
   # parser = reqparse.RequestParser()
   # parser.add_argument('price', 
   #         type = float,
   #         required = True,
   #         help = 'This field cannot be left blank!'
   #     )
   # parser.add_argument('store_id', 
   #         type = int,
   #         required = True,
   #         help = 'Every item needs a store id.'
   #     )
    

    def get(self, name):
        store = store_model_module.StoreModel.find_by_name(name)
        if store:
            return store.json()
        return {'message': 'Store not found'}, 404
    
    
    def post(self, name):
        if store_model_module.StoreModel.find_by_name(name):
            return { 'message' : "A store with name '{}' already exists." .format(name)}, 400
        
        #data = Store.parser.parse_args()
        
        store = store_model_module.StoreModel(name)
        
        
        try: 
            store.save_to_db()
        except:
            return {'message': 'An error occured while inserting the store.'}, 500 # internal server error
        
        
        return store.json(), 201
    
    
    def delete(self, name):
        store = store_model_module.StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()
        
        return {'message': 'Store deleted'}
    

    

    
class StoreList(Resource):
    def get(self):
        return {'stores': [store.json() for store in store_model_module.StoreModel.query.all()]}
    
    
    
    
    
    