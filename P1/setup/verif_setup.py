import psycopg2
# Try to connect to your Postgres instance (update user/password/db)
try:
    conn = psycopg2.connect(
        dbname="db_junior", 
        user="junior_user", 
        password="junior_db1693", 
        host="localhost"
    )
    print("Environment Ready: Database driver active.")
    conn.close()
except Exception as e:
    print(f"Setup needed: {e}")