import pandas as pd 
import sqlite3

conn = sqlite3.connect('buddymove_holidayiq.sqlite3')


df = pd.read_csv('https://raw.githubusercontent.com/jakekrafczyk/DS-Unit-3-Sprint-2-SQL-and-Databases/master/module1-introduction-to-sql/buddymove_holidayiq.csv')
print(df.shape)

#df.to_sql('review',conn)
cursor = conn.cursor()
print("CURSOR", cursor)

query = "SELECT COUNT('index') from review;"
result = cursor.execute(query).fetchall()
print("n rows", result)

query2 = "SELECT COUNT(Picnic) FROM review WHERE Nature > 99 AND Picnic > 99;"
result2 = cursor.execute(query2).fetchall()
print("users reviewed", result2)
