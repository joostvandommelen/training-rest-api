# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 14:01:55 2019

@author: nldomme8
"""

from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required
#from user import UserRegister
import os


# run create_table.py 

os.chdir('C:/Users/nldomme8/Documents/Projecten/Flask_training')

sec = __import__('20191209-security')
item_mod = __import__('20191209_item')
user_mod = __import__('20191209-users')
store_mod = __import__('20191209_store')

db_module = __import__('20191209_db')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/nldomme8/Documents/data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'joost' # long and complicated
api = Api(app)


@app.before_first_request
def create_tables():
    db_module.db.create_all()



jwt = JWT(app, sec.authenticate, sec.identify) # /auth



    
api.add_resource(store_mod.Store, '/store/<string:name>')
api.add_resource(item_mod.Item, '/item/<string:name>')
api.add_resource(item_mod.ItemList, '/items')
api.add_resource(store_mod.StoreList, '/stores')
api.add_resource(user_mod.UserRegister, '/register')

if __name__ == '__main__':
    db_module.db.init_app(app)
    app.run(port=5000)
