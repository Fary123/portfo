from flask import Flask, render_template, redirect, request
import csv

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template('index.html')


@app.route('/project.html')
def html_page2():
    return render_template('project.html')


@app.route('/index.html')
def html_page():
    return render_template('index.html')


@app.route('/thankyou.html')
def html_page3():
    return render_template('thankyou.html')



def write_to_csv(data):
    with open('database.csv', newline="", mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])

@app.route('/submit_form', methods=['POST','GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect('/thankyou.html')
    else:
        return "Something wrong"

