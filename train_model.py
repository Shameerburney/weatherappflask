from sklearn.linear_model import LinearRegression
import pickle

# 🧠 Example dataset: [humidity, wind_speed] -> temperature
X = [
    [30, 2],
    [45, 3],
    [60, 5],
    [75, 4],
    [85, 1],
    [90, 2.5],
    [50, 3.5],
    [40, 2.2],
    [70, 4.8],
    [65, 3.1]
]

y = [35, 32, 28, 26, 25, 24, 30, 33, 27, 29]

# 🔧 Train model
model = LinearRegression()
model.fit(X, y)

# 💾 Save model to file
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("✅ Model trained and saved as model.pkl")
