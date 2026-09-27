import joblib
import pandas as pd
from config.paths_config import MODEL_OUTPUT_PATH
from flask import Flask, render_template, request

app = Flask(__name__)

loaded_model = joblib.load(MODEL_OUTPUT_PATH)
FEATURES = list(loaded_model.feature_name_)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        row = {name: float(request.form[name]) for name in FEATURES}
        features = pd.DataFrame([row], columns=FEATURES)

        prediction = loaded_model.predict(features)

        return render_template('index.html', prediction=prediction[0])

    return render_template("index.html", prediction=None)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
