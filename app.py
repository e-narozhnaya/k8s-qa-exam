from flask import Flask

app = Flask(__name__)

# Мы заставляем Flask брать настройки из окружения (из твоего YAML или Docker)
# Если переменной нет, он возьмет значение по умолчанию (например, 'localhost')
app.config['MYSQL_HOST'] = os.environ.get('MYSQL_HOST', 'mysql-service')
app.config['MYSQL_USER'] = os.environ.get('MYSQL_USER', 'root')
app.config['MYSQL_PASSWORD'] = os.environ.get('MYSQL_PASSWORD', 'mypassword')
app.config['MYSQL_DB'] = os.environ.get('MYSQL_DB', 'dockerdb')
# ---------------------------

@app.route('/')
def hello():
    return 'Docker KP2 task 1 says: You did it! Well done!'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
