# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 10:49:40 2019

@author: nldomme8
"""
if False:
    import sqlite3
    
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    
    create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"
    cursor.execute(create_table)
    
    
    create_table = "CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, name text, price real)"
    cursor.execute(create_table)
    
    #cursor.execute("INSERT INTO items VALUES ('test', 10.99)")
    
    connection.commit()
    connection.close()