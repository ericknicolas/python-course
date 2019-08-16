#import psycopg2
import psycopg2

def create_table():
    conn = psycopg2.connect("dbname='bookstore' user='postgres' password='Eri1ck444' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

def inster(item, quantity, price):
    conn = psycopg2.connect("dbname='bookstore' user='postgres' password='Eri1ck444' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES (%s, %s, %s)", (item, quantity, price))
    conn.commit()
    conn.close()

def view():
    conn = psycopg2.connect("dbname='bookstore' user='postgres' password='Eri1ck444' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(item):
    conn = psycopg2.connect("dbname='bookstore' user='postgres' password='Eri1ck444' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item=%s", (item,))
    conn.commit()
    conn.close()

def update(quantity, price, item):
    conn = psycopg2.connect("dbname='bookstore' user='postgres' password='Eri1ck444' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity=%s, price=%s WHERE item=%s", (quantity, price, item))
    conn.commit()
    conn.close()


#create_table()
#inster("orange glass", 20, 80)
#delete("orange glass")
update(5, 11, "wine glass")
print(view())
