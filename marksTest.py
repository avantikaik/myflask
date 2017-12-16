from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/entermarks')
@app.route('/')
def home():
    return render_template('students_marks.html')
    #run the script and navigate to http://localhost:5000 or http://localhost:5000/entermarks
    #enter the marks and submit..
    #control goes to http://localhost:5000/view page and data will flow from studends_marks.html to viewmarks.html page.

@app.route('/view', methods = ['POST'])
def mks():
    if request.method == 'POST':
        try:
            maks = int(request.form['ma'])
        except Exception:
            print("check the input and try again")
        else:
            return render_template('viewmarks.html', marks_entered = maks)
if __name__== '__main__':
    app.run()