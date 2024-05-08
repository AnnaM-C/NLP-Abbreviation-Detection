import pickle
import spacy
import json

def word2features(sentence: list, i: int):
    word = sentence[i]
    features = {
        'word': word,
        'is_first': i == 0,  # if the word is a first word
        'is_last': i == len(sentence) - 1,  #if the word is a last word
        'is_capitalized': word[0].upper() == word[0],
        'is_all_caps': word.upper() == word,  #word is in uppercase
        'is_all_lower': word.lower() == word,  #word is in lowercase
        #prefix of the word
        'prefix-1': word[0],
        'prefix-2': word[:2],
        'prefix-3': word[:3],
        #suffix of the word
        'suffix-1': word[-1],
        'suffix-2': word[-2:],
        'suffix-3': word[-3:],
        #extracting previous word
        'prev_word': '' if i == 0 else sentence[i - 1][0],
        #extracting next word
        'next_word': '' if i == len(sentence) - 1 else sentence[i + 1][0],
        'has_hyphen': '-' in word,  #if word has hypen
        'is_numeric': word.isdigit(),  #if word is in numeric
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
        tokens = [token.text for token in self.en_nlp.tokenizer(sentence)]
        sentence_features = sent2features(tokens)
        prediction = self.crf.predict([sentence_features])[0]
        return {
            "prediction": json.dumps(prediction),
            "tokens": json.dumps(tokens)
        }


if __name__ == '__main__':
    predictor = Predictor()
    predictor.load_model()

    # inference
    example_sentence = 'Abbreviations: GEMS, Global Enteric Multicenter Study; VIP, ventilated improved pit.'
    example_prediction = predictor.predict(example_sentence)
    print(example_prediction)
