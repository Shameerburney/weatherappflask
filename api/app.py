import os
from flask import Flask, render_template, request
import pickle

app = Flask(__name__, template_folder=os.path.join(os.path.dirname(__file__), 'templates'))

MODEL_PATH = os.path.join(os.path.dirname(__file__), 'model.pkl')
with open(MODEL_PATH, 'rb') as f:
    model = pickle.load(f)

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    if request.method == 'POST':
        try:
            humidity = float(request.form.get('humidity'))
            wind_speed = float(request.form.get('wind_speed'))
            prediction = model.predict([[humidity, wind_speed]])[0]
        except Exception as e:
            prediction = f"Error: {e}"
    return render_template('index.html', prediction=prediction)
