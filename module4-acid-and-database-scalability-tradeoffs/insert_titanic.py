# INSERTING TITANIC DATASET INTO POSTGRESQL

import os
from dotenv import load_dotenv
import json
import psycopg2
import pandas as pd
from psycopg2.extras import execute_values

load_dotenv() #> loads contents of the .env file into the script's environment

DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
print(DB_NAME)

connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
print("CONNECTION:", connection)

df = pd.read_csv('https://raw.githubusercontent.com/jakekrafczyk/DS-Unit-3-Sprint-2-SQL-and-Databases/master/module2-sql-for-analysis/titanic.csv')

tuples = list(df.itertuples(index=False,name=None))
#print(tuples)

cursor = connection.cursor()
print("CURSOR:", cursor)

#insertion_query = 'INSERT INTO titan_table (survived,pclass,name,sex,age,siblings_or_spouse,parents_or_children,fare) VALUES %s'
#execute_values(cursor,insertion_query,tuples)

connection.commit()

#execute queries
cursor.execute('SELECT COUNT(name) FROM titan_table')
result = cursor.fetchall()
print("RESULT:", type(result))
print(result)

# How many passengers survived, and how many died?
cursor.execute("SELECT COUNT(name) FROM titan_table WHERE survived='1';")
result = cursor.fetchall()
print("RESULT:", type(result))
print(result)

# How many passengers were in each class?
cursor.execute("SELECT COUNT(name) FROM titan_table GROUP BY pclass;")
result = cursor.fetchall()
print("RESULT:", type(result))
print(result)

# How many passengers survived/died within each class?
cursor.execute("SELECT COUNT(survived) FROM titan_table WHERE survived='1' GROUP BY pclass;")
result = cursor.fetchall()
print("RESULT:", type(result))
print(result)

cursor.execute("SELECT COUNT(survived) FROM titan_table WHERE survived='0' GROUP BY pclass;")
result = cursor.fetchall()
print("RESULT:", type(result))
print(result)

# What was the average age of survivors vs nonsurvivors?
#cursor.execute("SELECT AVG(age) FROM titan_table;")
#result = cursor.fetchall()      # numbers are stored wrong, should be an int type
#print("RESULT:", type(result))
#print(result)

# Do any passengers have the same name?
cursor.execute("SELECT name, COUNT(*) FROM titan_table GROUP BY name HAVING COUNT(*) > 1;")
result = cursor.fetchall()
print("DUPS:", type(result))
print(result)