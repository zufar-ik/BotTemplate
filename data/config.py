import psycopg2
from environs import Env

# Используем библиотеку environs
env = Env()
env.read_env()
con = psycopg2.connect(
    database=env.str('POSTGRES_DB'),
    user=env.str('POSTGRES_USER'),
    password=env.str('POSTGRES_PASSWORD'),
    host=env.str('POSTGRES_HOST'),
    port=env.str('POSTGRES_PORT')
)
# Считываем данные из .env
cur = con.cursor()
cur.execute("SELECT * from main_bottoken")
token = cur.fetchall()
BOT_TOKEN = token[0][1]  # Токен бота

cur = con.cursor()
cur.execute("SELECT * from main_botadmin")
rows = cur.fetchall()
ADMINS = []

for i in rows:
    ADMINS.append(i[1])

DB_USER = env.str("POSTGRES_USER")
DB_PASS = env.str("POSTGRES_PASSWORD")
DB_NAME = env.str("POSTGRES_DB")
DB_HOST = env.str("POSTGRES_HOST")
con.close()

