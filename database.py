import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="level2_booking",
    user="postgres",
    password="059254",
    port="5432"
)

cursor = conn.cursor()