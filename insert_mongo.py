
import pymongo
import os
from dotenv import load_dotenv
import pandas as pd
import sqlite3

DB_FILEPATH = os.path.join(os.path.dirname(__file__),  "module1-introduction-to-sql/rpg_db.sqlite3")

connection = sqlite3.connect(DB_FILEPATH)
print("CONNECTION:", connection)

cursor = connection.cursor()
print("CURSOR", cursor)

query = "SELECT * FROM charactercreator_character;"
charactercreator_character = cursor.execute(query).fetchall()
#print("Q1", result)

rpgs = ['armory_item', 'armory_weapon', 'charactercreator_character_inventory','charactercreator_cleric',
        'charactercreator_fighter', 'charactercreator_mage', 'charactercreator_necromancer',
        'charactercreator_thief']

load_dotenv()

DB_USER = os.getenv("MONGO_USER", default="OOPS")
DB_PASSWORD = os.getenv("MONGO_PASSWORD", default="OOPS")
CLUSTER_NAME = os.getenv("MONGO_CLUSTER_NAME", default="OOPS")

connection_uri = f"mongodb+srv://{DB_USER}:{DB_PASSWORD}@{CLUSTER_NAME}.mongodb.net/test?retryWrites=true&w=majority"
print("----------------")
print("URI:", connection_uri)

client = pymongo.MongoClient(connection_uri)
print("----------------")
print("CLIENT:", type(client), client)

db = client.test_database # "test_database" or whatever you want to call it
print("----------------")
print("DB:", type(db), db)

for table in rpgs:
    query = f"SELECT * FROM {table};"
    rpg_table = cursor.execute(query).fetchall()
    print(rpg_table)
    #doesnt work
    rpg_dict = dict(rpg_table)

    collection = db.table # "pokemon_test" or whatever you want to call it
    print("----------------")
    print("COLLECTION:", type(collection), collection)

    print("----------------")
    print("COLLECTIONS:")
    print(db.list_collection_names())

    

    db.things.insert_many(rpg_table)

print("DOCS:", collection.count_documents({}))
print(collection.count_documents({"name": "Qui"}))

# Mongo has more flexibiity when inserting data, but its webisites configuration is confusing.