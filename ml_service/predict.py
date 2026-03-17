import joblib

model = joblib.load("ml_service/model.pkl")

def predict(data):
    return model.predict([data]).tolist()