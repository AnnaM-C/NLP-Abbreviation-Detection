import csv
from datetime import datetime
import logging

from flask import Flask, request, render_template, jsonify

from predictor import Predictor


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

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

    data = request.get_json()

    if not data or 'input' not in data:
        logger.error("No sentence provided in the request data.")
        return jsonify({"error": "No sentence provided"}), 422

    input_sentence = data['input'].strip()

    try:
        prediction_obj = predictor.predict(input_sentence)
    except ValueError as e:
        logger.error(f"An error occurred while predicting the sentence: {str(e)}")
        return jsonify({"error": str(e)}), 422
    except Exception as e:
        logger.error(f"An unexpected error occurred while predicting the sentence: {str(e)}")
        return jsonify({"error": "An unexpected error occurred."}), 400
    
    logger.info("Prediction successful")

    with open("monitor_log.csv", mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([input_sentence, prediction_obj['tokens'], prediction_obj['prediction'], cur_time])

    return prediction_obj


if __name__ == '__main__':
    app.run(debug=True)
