import pickle
import spacy
import json
from flask import Flask, request, jsonify
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def word2features(sentence: list, i: int):
    word = sentence[i]
    features = {
        'word': word,
        'is_first': i == 0,
        'is_last': i == len(sentence) - 1,
        'is_capitalized': word[0].upper() == word[0],
        'is_all_caps': word.upper() == word,
        'is_all_lower': word.lower() == word,
        'prefix-1': word[0],
        'prefix-2': word[:2],
        'prefix-3': word[:3],
        'suffix-1': word[-1],
        'suffix-2': word[-2:],
        'suffix-3': word[-3:],
        'prev_word': '' if i == 0 else sentence[i - 1][0],
        'next_word': '' if i == len(sentence) - 1 else sentence[i + 1][0],
        'has_hyphen': '-' in word,
        'is_numeric': word.isdigit(),
        'capitals_inside': word[1:].lower() != word[1:]
    }
    return features

def sent2features(tokens: list):
    return [word2features(tokens, index) for index in range(len(tokens))]

class Predictor:
    def __init__(self):
        self.crf = None
        self.en_nlp = spacy.load("en_core_web_sm")

    def load_model(self):
        with open('crf_model.pkl', 'rb') as file:
            self.crf = pickle.load(file)

    def predict(self, sentence):
        if not sentence:
            raise ValueError("Input sentence is empty.")
        
        tokens = [token.text for token in self.en_nlp.tokenizer(sentence)]
        
        if len(tokens) > 512:
            raise ValueError("Input sentence exceeds the word limit of 512 words.")
        
        sentence_features = sent2features(tokens)
        prediction = self.crf.predict([sentence_features])[0]
        return {
            "prediction": json.dumps(prediction),
            "tokens": json.dumps(tokens)
        }

app = Flask(__name__)
predictor = Predictor()
predictor.load_model()

@app.route('/predict', methods=['POST'])
def get_prediction():
    try:
        data = request.get_json()
        if not data or 'sentence' not in data:
            logger.error("No sentence provided in the request data.")
            return jsonify({"error": "No sentence provided"}), 400

        sentence = data['sentence'].strip()
        
        prediction_obj = predictor.predict(sentence)
        logger.info("Prediction successful")
        return jsonify(prediction_obj)
    except ValueError as e:
        logger.error(f"ValueError: {str(e)}")
        return jsonify({"error": str(e)}), 422
    except Exception as e:
        logger.error(f"An unexpected error occurred: {str(e)}")
        return jsonify({"error": "An unexpected error occurred."}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
