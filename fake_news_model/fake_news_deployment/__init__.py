import logging
import re
from string import punctuation
import contractions
import azure.functions as func
import pandas as pd
import joblib
import json
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences


def processing(sample_data):
    # Text Cleaning
    # Remove extra spaces, tabs, and line breaks
    sample_data = " ".join(sample_data.split())
    # Remove punctuation
    sample_data = re.sub(f"[{re.escape(punctuation)}]", "", sample_data)
    # Remove numbers
    sample_data = re.sub(r"\b[0-9]+\b\s*", "", sample_data)
    # Remove non-alphabetic characters and extra spaces
    sample_data = " ".join([w for w in sample_data.split() if w.isalpha()])

    # Expand contractions and then convert to lower-case.
    word_list = []
    for each_word in sample_data.split(' '):
        try:
            word_list.append(contractions.fix(each_word).lower())
        except:
            print("Error in contractions")
    sample_data = " ".join(word_list)
    sample_df = pd.DataFrame([sample_data], columns=['all_info'])

    # Word Tokenization
    # Replace out of vocabulary token using oov_token=<OOV>
    # Creates a vocabulary index based on word frequency
    tokenizer = Tokenizer(oov_token="<OOV>", num_words=6000)
    # Fit the tokenizer on the texts and convert them into
    # sequences of integers which uses the vocabulary index
    # created by fitting the tokenizer
    tokenizer.fit_on_texts(sample_df['all_info'])
    max_length = 40
    vocab_size = 6000
    sequences_sample = tokenizer.texts_to_sequences(sample_df['all_info'])
    padded_sample = pad_sequences(sequences_sample, padding='post', maxlen=max_length)

    fake_news_model = joblib.load('fake_news_model_pipe.pkl')

    prediction = (fake_news_model.predict(padded_sample) > 0.5).astype("int32")
    return prediction


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    data = req.get_json()
    data = json.loads(data)

    if data is not None:

        response = []
        prediction = processing(data[0]['text'])

        results_dict = {
            'prediction': int(prediction),
        }
        response.append(results_dict)

        return json.dumps(response)

    else:
        return func.HttpResponse(
            "Please pass a properly formatted JSON object to the API",
            status_code=400
        )
