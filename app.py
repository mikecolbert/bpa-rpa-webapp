from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

contact_list = ['test tester']

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html', pageTitle='BPA RPA Assignment',  contacts = contact_list)

@app.route('/add', methods=['POST'])
def add():
    print('in add')
    if request.method == 'POST':
        print("inside post")
        print(contact_list)
        form = request.form
        name = form['my_name']
        print(name)
        contact_list.append(name)
        print(contact_list)
        return redirect(url_for('index'))
        #return render_template('index.html', pageTitle='BPA RPA Assignment', contacts = contact_list) 
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
