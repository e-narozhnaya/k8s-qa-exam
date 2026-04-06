from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Docker KP2 task 1 says: You did it! Well done!'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
