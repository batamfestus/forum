from flask import Flask, render_template, url_for, request, redirect
import csv


app = Flask(__name__)


def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as database2:
        name = data['name']
        email = data['email']
        phone = data['phone']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        csv_writer.writerow([name,email,phone,message])

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/programs')
def programs():
    return render_template('programs.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/submit_form', methods=['GET', 'POST'])
def submit_form():
    
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect(url_for('success'))
        except:
            return 'Did not save to database!!!!!!'
    else:
        print('sorry, something went wrong.')

if __name__ == "__main__":
    app.run(debug=True)