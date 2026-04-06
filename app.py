import os
import pymysql
from flask import Flask

app = Flask(__name__)

# Мы заставляем Flask брать настройки из окружения (из твоего YAML или Docker)
# Если переменной нет, он возьмет значение по умолчанию (например, 'localhost')
app.config['MYSQL_HOST'] = os.environ.get('MYSQL_HOST', 'mysql-service')
app.config['MYSQL_USER'] = os.environ.get('MYSQL_USER', 'root')
app.config['MYSQL_PASSWORD'] = os.environ.get('MYSQL_PASSWORD', 'mypassword')
app.config['MYSQL_DB'] = os.environ.get('MYSQL_DB', 'dockerdb')
# ---------------------------

def get_db_connection():
    return pymysql.connect(
        host=app.config['MYSQL_HOST'],
        user=app.config['MYSQL_USER'],
        password=app.config['MYSQL_PASSWORD'],
        database=app.config['MYSQL_DB'],
        cursorclass=pymysql.cursors.DictCursor
    )

@app.route('/')
def hello():
    try:
        conn = get_db_connection()
        conn.close()
        db_status = "Successfully connected to the database!"
    except Exception as e:
        db_status = f"Failed to connect to the database: {str(e)}"
        
    return f'Docker KP2 task 1 says: You did it! Well done!<br>DB Status: {db_status}'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
