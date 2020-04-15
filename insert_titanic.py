

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

insertion_query = 'INSERT INTO titan_table (survived,pclass,name,sex,age,siblings_or_spouse,parents_or_children,fare) VALUES %s'
execute_values(cursor,insertion_query,tuples)

connection.commit()

cursor.execute('SELECT COUNT(name) FROM titan_table')
result = cursor.fetchall()
print("RESULT:", type(result))
print(result)

