import json
import pickle
import spacy


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
