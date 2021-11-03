from flask import Flask
app = Flask(__name__)
@app.route('/')

def hello_flask():
    return 'Hello world from flask'

@app.route('/apache')

def hello_apache():
    return 'Hello world from Apache'

if __name__ == '__main__':
    app.run()

