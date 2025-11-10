from flask import Flask, render_template, request
import pickle
import os

# Correct template folder path
app = Flask(__name__, template_folder='../templates')

# Load the trained model safely
MODEL_PATH = os.path.join(os.path.dirname(__file__), '../model.pkl')
try:
    with open(MODEL_PATH, 'rb') as f:
        model = pickle.load(f)
except FileNotFoundError:
    model = None
    print(f"Warning: model.pkl not found at {MODEL_PATH}")

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    if request.method == 'POST' and model:
        try:
            humidity = float(request.form.get('humidity'))
            wind_speed = float(request.form.get('wind_speed'))
            prediction = model.predict([[humidity, wind_speed]])[0]
        except Exception as e:
            prediction = f"Error: {e}"
    elif request.method == 'POST' and not model:
        prediction = "Model not loaded."

    return render_template('index.html', prediction=prediction)

# Remove app.run() block for Vercel
# Vercel automatically serves the Flask app
