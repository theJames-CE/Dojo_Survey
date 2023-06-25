from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'James wuz here!'

# Put the form data into session
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        session['name'] = request.form['name']
        session['location'] = request.form['location']
        session['languages'] = request.form['languages']
        session['gender'] = request.form['gender']
        session['checkboxes'] = request.form.getlist('checkboxes[]')
        session['comments'] = request.form['comments']
        return redirect(url_for('result'))
    return render_template('index.html')

# Put the form data into session
@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        session['name'] = request.form['name']
        session['location'] = request.form['location']
        session['languages'] = request.form['languages']
        session['gender'] = request.form['gender']
        session['checkboxes'] = request.form.getlist('checkboxes[]')
        session['comments'] = request.form['comments']
        return redirect(url_for('result'))

    if 'name' in session:
        name = session['name']
        location = session['location']
        languages = session['languages']
        gender = session['gender']
        checkboxes = session.get('checkboxes', [])
        comments = session['comments']
        return render_template('result.html', name=name, location=location, languages=languages, gender=gender,checkboxes=checkboxes, comments=comments)

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()
