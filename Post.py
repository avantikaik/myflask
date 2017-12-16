from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)
@app.route('/success/<name>')
def success(name):
    return 'Welcome %s' % name

@app.route('/home')
@app.route('/')
@app.route('/Randomname')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method=='POST':
        user = request.form['nm']
        # return redirect(url_for('success', name=user))        #success is a method
        return render_template('home.html', name_entered=user)
    else:
        user = request.args.get('nm')
        return redirect(url_for('success', name=user))



if __name__== '__main__':
    app.run()


