import psycopg2

# Connect to your postgres DB
conn = psycopg2.connect("patricknelson=test user=patricknelson")

conn.set_session(autocommit=True)
# Open a cursor to perform database operations
cur = conn.cursor()
# Execute a query
cur.execute('SELECT * FROM "consoles"')