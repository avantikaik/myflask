from flask import Flask

app = Flask(__name__)


@app.route('/hello')
def hello_world():
    return 'Hello World!'

@app.route('/')
def hello_default():
    return 'Hello Default/!'

def add_url_method_name():
    return 'add url method'
app.add_url_rule('/addurl', 'add', add_url_method_name)

def variable_part(name):
    return 'Hello variable part: %s'% name
app.add_url_rule('/var/<name>', 'var', variable_part)

if __name__ == '__main__':
    app.run()



# http://127.0.0.1:5000/