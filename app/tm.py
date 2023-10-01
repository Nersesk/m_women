import psycopg2

conn = psycopg2.connect(
    database='postgres',
    user='postgres',
    password='4145',
    host='localhost',
    port='5432',
    options='-c search_path=public',
    connect_timeout=10,
)