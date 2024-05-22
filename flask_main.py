from flask import Flask, request, render_template, jsonify
from datetime import datetime
from predictor import Predictor
import csv

app = Flask(__name__, template_folder='templates')

predictor = Predictor()
predictor.load_model()


# hope page to load template for model inputs and display outputs
@app.route('/')
def home():
    return render_template('home.html')


@app.route('/predict', methods=['POST'])
def predict():
    cur_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    input_sentence = request.json['input']
    prediction_obj = predictor.predict(input_sentence)
    if prediction_obj == "":
        with open("monitor_log.csv", mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([input_sentence, "", "", cur_time])

    with open("monitor_log.csv", mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([input_sentence, prediction_obj['tokens'], prediction_obj['prediction'], cur_time])

    return prediction_obj


if __name__ == '__main__':
    app.run(debug=True)
