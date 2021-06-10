import psycopg2 

# Connect to the db
conn = psycopg2.connect(
        host="localhost",
        port="5432",
        user="charlie",
        database="zoo_animals"
)

# Cursor
cur = conn.cursor()

cur.execute("select id, species_name from species")

rows = cur.fetchall()

for r in rows:
    print(f"id {r[0]} species {r[1]}")

# Close the cursor
cur.close()

# Close the connection
conn.close()

# Leaking is the worst