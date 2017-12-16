from flask import Flask, url_for, flash, request, render_template

app = Flask(__name__)
@app.route('/')
@app.route('/empDetails')
def emp_details():
    return render_template('empdata.html')

@app.route('/viewEmployeeData', methods=['POST'])
def viewEMPData():
    if(request.method=='POST'):
        result1 = request.form

        return render_template('view_emp_details.html', result=result1)

if __name__== '__main__':
    app.run()

