# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 16:24:41 2019

@author: nldomme8
"""

if False: 
    import sqlite3
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    create_table = "CREATE TABLE users (id int, username text, password text)"
    cursor.execute(create_table)
    
    user = (1, "jose", "asdf")
    insert_query = "INSERT INTO users VALUES (?, ?, ?)"
    cursor.execute(insert_query, user)
    
    users = [(2, 'rolf', 'asdf'),
             (3, 'anne', 'xyz')]
    cursor.executemany(insert_query, users)
    
    connection.commit()
    connection.close()



import sqlite3
import os
from flask_restful import Resource, reqparse
os.chdir('C:/Users/nldomme8/Documents/Projecten/Flask_training')
user_model_module = __import__('20191209_user_model')




class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username', 
        type = str, 
        required = True,
        help='This field cannot be blank.'
    )
    
    parser.add_argument('password', 
        type = str, 
        required = True,
        help='This field cannot be blank.'
    )
    
    
    def post(self):
        data = UserRegister.parser.parse_args()
        
        if user_model_module.UserModel.find_by_username(data['username']):
            return {'message':'A user with that username already exists.'}, 400
        
        user = user_model_module.UserModel(**data)
        user.save_to_db()
        
        return {"message": "User created succesfully."}, 201
    
        