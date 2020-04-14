import os
import sqlite3

# construct a path to wherever your database exists
#DB_FILEPATH = "chinook.db"
DB_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "Downloads/rpg_db.sqlite3")

connection = sqlite3.connect(DB_FILEPATH)
print("CONNECTION:", connection)

cursor = connection.cursor()
print("CURSOR", cursor)

#question 1 - total characters count
query = "SELECT COUNT(DISTINCT character_id) AS character_count FROM charactercreator_character;"
result = cursor.execute(query).fetchall()
print("Q1", result)

#question 2 - subclasses count
query2 = "SELECT COUNT(DISTINCT character_ptr_id) AS cleric_count FROM charactercreator_cleric;"
query3 = "SELECT COUNT(DISTINCT character_ptr_id) AS fighter_count FROM charactercreator_fighter;"
query4 = "SELECT COUNT(DISTINCT character_ptr_id) AS mage_count FROM charactercreator_mage;"
query5 = "SELECT COUNT(DISTINCT mage_ptr_id) AS necromancer_count FROM charactercreator_necromancer;"
query6 = "SELECT COUNT(DISTINCT character_ptr_id) AS thief_count FROM charactercreator_thief;"

result2 = cursor.execute(query2).fetchall()
print("cleric", result2)
result3 = cursor.execute(query3).fetchall()
print("fighter", result3)
result4 = cursor.execute(query4).fetchall()
print("mage", result4)
result5 = cursor.execute(query5).fetchall()
print("necro", result5)
result6 = cursor.execute(query6).fetchall()
print("theif", result6)

#question 3 - total items
query7 = "SELECT COUNT(DISTINCT item_id) AS item_count FROM armory_item;"
result7 = cursor.execute(query7).fetchall()
print('items',result7[0][0])

#question 4 - how many weapons?
query8 = "SELECT COUNT(DISTINCT item_ptr_id) AS weapon_count FROM armory_weapon;"
result8 = cursor.execute(query8).fetchall()
print('weapons',result8[0][0])
print('non weapons',(result7[0][0]-result8[0][0]))

#question 5 - how many items for each character
query9 = "SELECT character_id, COUNT(DISTINCT item_id) AS items_count FROM charactercreator_character_inventory GROUP BY character_id;"
result9 = cursor.execute(query9).fetchall()
print('character items',result9[0:20])

#question 6 - how many weapons for each?
query10 = "SELECT item_ptr_id AS weapons FROM armory_weapon;"
result10 = cursor.execute(query10).fetchall()
#print('weapon_ids', result10[0:20])

query11 = "SELECT character_id, COUNT(DISTINCT item_id) AS char_weapons_count FROM charactercreator_character_inventory GROUP BY character_id HAVING item_id > 137;"
result11 = cursor.execute(query11).fetchall()
print('character weapons', result11[0:20])

#question 7 -  average items for character
query12 = "SELECT COUNT(item_id) AS char_item_count FROM charactercreator_character_inventory;"
result12 = cursor.execute(query12).fetchall()
#print('items',result12[0][0])

print('avg items per character', result12[0][0] / result[0][0])

#question 8 - average weapons per character
query13 = "SELECT COUNT(item_id) AS weapons_count FROM charactercreator_character_inventory GROUP BY id HAVING item_id > 137;"
result13 = cursor.execute(query13).fetchall()
#print('weapon count', len(result13))

print('avg weapons per character', len(result13) / result[0][0])