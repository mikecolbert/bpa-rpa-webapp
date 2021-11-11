from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

contact_list = [{"name": "Testy Testerton", "email": "test@test.com"} ]

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html', pageTitle='BPA RPA Assignment',  contacts = contact_list)

@app.route('/add', methods=['POST'])
def add():
    print('in add')
    if request.method == 'POST':
        form = request.form
        fname = form['fname']
        lname = form['lname']
        email = form['email']
        print(fname)
        print(lname)
        name_dict = {"name": fname + " " + lname, "email": email}
        print(name_dict)
        contact_list.append(name_dict)
        print(contact_list)
        return redirect(url_for('index'))
        #return render_template('index.html', pageTitle='BPA RPA Assignment', contacts = contact_list) 
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
