from flask import Flask, session, request, render_template, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'testing'

@app.route('/')
@app.route('/login')
def login_test():
    return render_template('sessionHTML.html')

@app.route('/session-page', methods=['POST'])
def session_transfer_page():
    if(request.method=='POST'):
        session['username'] = request.form['user']
        result = request.form
        print("session data saved to server: "+ session['username'])
        return render_template('session-home.html', result=result)




@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login_test'))

if __name__== '__main__':
    app.run(debug=True)

