import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

# 🧠 Example dataset (humidity, wind_speed, temperature)
data = {
    'humidity': [30, 45, 60, 75, 85, 90, 50, 40, 70, 65],
    'wind_speed': [2, 3, 5, 4, 1, 2.5, 3.5, 2.2, 4.8, 3.1],
    'temperature': [35, 32, 28, 26, 25, 24, 30, 33, 27, 29]
}

df = pd.DataFrame(data)

# 🔍 Features (X) and target (y)
X = df[['humidity', 'wind_speed']]
y = df['temperature']

# 🔧 Train model
model = LinearRegression()
model.fit(X, y)

# 💾 Save model to file
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("✅ Model trained and saved as model.pkl")
