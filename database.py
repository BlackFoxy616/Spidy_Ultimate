import os

os.system("pip install psycopg2")


import psycopg2


conn = psycopg2.connect(database="emlvwsts",
                        host="mahmud.db.elephantsql.com",
                        user="emlvwsts",
                        password="QZplqRjrPc5y3n2cf6VwgdvhcUZJ1hXV",
                        port="5432")

cursor = conn.cursor()

def create_table():
  cursor.execute("DROP TABLE IF EXISTS Links")

  sql ='''CREATE TABLE Links(
   URL VARCHAR(255) NOT NULL,
   NAME VARCHAR(255) NOT NULL
)'''

  cursor.execute(sql)
  print("Table created successfully........")
  conn.commit()


def insert_db(link,names):
    query = "INSERT INTO Links (url,name) VALUES('{}','{}')".format(link,names)
    cursor.execute(query)
    conn.commit()

def read_db():
   cursor.execute("SELECT * FROM Links")
   data = cursor.fetchall()
   return data

def delall_db(name):
    cursor.execute(f"DELETE FROM {name}")
    conn.commit()




if 1==1:
  #insert_db("www.google.com","Google")
  for t in read_db():
      if "Goo" in t:
         print(t)