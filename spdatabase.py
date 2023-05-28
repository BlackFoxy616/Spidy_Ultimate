try:
  import psycopg2
except:
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
  cursor.execute("DROP TABLE IF EXISTS PHLinks")

  sql ='''CREATE TABLE PHLinks(
   LINK VARCHAR(255) NOT NULL
)'''

  cursor.execute(sql)
  print("Table created successfully........")
  conn.commit()


def insert_db(ln):
    query = "INSERT INTO PHLinks (link) VALUES(%s);"
    data = (ln,)
    cursor.execute(query,data)
    conn.commit() 

def read_db():
   cursor.execute("SELECT * FROM PHLinks")
   data = cursor.fetchall()
   conn.commit()
   return data

def delall_db(name):
    cursor.execute(f"DELETE FROM {name}")
    conn.commit()


def read_links():
   cursor.execute("SELECT * FROM dled")
   data = cursor.fetchall()
   conn.commit()
   return data



def insert_links(ln):
    query = "INSERT INTO dled (link) VALUES(%s);"
    data = (ln,)
    cursor.execute(query,data)
    conn.commit() 




