# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 16:18:02 2019

@author: nldomme8
"""
import os
os.chdir('C:/Users/nldomme8/Documents/Projecten/Flask_training')
#from 20191209-users import User

user_model_module = __import__('20191209_user_model')

#users = [
#       users_mod.User(1, 'bob', 'asdf')
#        ]


#username_mapping = {u.username: u for u in users}
#userid_mapping = {u.id: u for u in users}
        


def authenticate(username,password):
    user = user_model_module.UserModel.find_by_username(username)
    if user and user.password == password:
        return user
    
    
def identify(payload):
    user_id = payload['identity']
    return user_model_module.UserModel.find_by_id(user_id)