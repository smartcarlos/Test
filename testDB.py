import psycopg2
conn=psycopg2.connect(database="db_person1", user="postgres", password="a2020", host="127.0.0.1", port="5432")
cur = conn.cursor()
cur.execute("CREATE TABLE test(id serial PRIMARY KEY, num integer,data varchar);")
cur.execute("INSERT INTO test(num, data)VALUES(%s, %s)", (1, 'aaa'))
cur.execute("INSERT INTO test(num, data)VALUES(%s, %s)", (2, 'bbb'))
cur.execute("INSERT INTO test(num, data)VALUES(%s, %s)", (3, 'ccc'))
cur.execute("SELECT * FROM test;")
rows = cur.fetchall()
print(rows)
for i in rows:
  print(i)
conn.commit()
cur.close()
conn.close() 
Di Yi Ci