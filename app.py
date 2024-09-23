  GNU nano 8.2                              app.py
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    # Get user inputs
    altitude = float(request.form['altitude'])
    frequency = float(request.form['frequency'])
    power = float(request.form['power'])
    gain = float(request.form['gain'])

    # Perform calculations (simplified example)
    eirp = power + gain  # EIRP calculation

    return render_template('index.html', eirp=eirp)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')