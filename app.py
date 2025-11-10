from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# 🧠 Load trained model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None

    if request.method == 'POST':
        try:
            humidity = float(request.form.get('humidity'))
            wind_speed = float(request.form.get('wind_speed'))
            # 🔮 Predict temperature
            prediction = model.predict([[humidity, wind_speed]])[0]
        except Exception as e:
            prediction = f"Error: {e}"

    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
