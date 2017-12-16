from flask import Flask, render_template, request, flash
from forms import ContactForm
app = Flask(__name__)
app.secret_key = 'dev key- some random text'


@app.route('/contact', methods=['POST', 'GET'])
def contact():
    form = ContactForm()
    render_template('contact.html', form=form)
    if request.method == 'POST':
        if form.validate() == False:
            flash('Enter all the mandatory(*) fields')
            return render_template('contact.html', form=form)
        else:
            return render_template('success.html')
    elif request.method == 'GET':
        return render_template('contact.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)



