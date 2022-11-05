import pickle
# from sklearn.feature_extraction.text import CountVectorizer
# import plotly.express as px
# import pandas as pd
import csv
from pandas import *
import re


cEXT = pickle.load(open("Datasets/models/cEXT.p", "rb"))
cNEU = pickle.load(open("Datasets/models/cNEU.p", "rb"))
cAGR = pickle.load(open("Datasets/models/cAGR.p", "rb"))
cCON = pickle.load(open("Datasets/models/cCON.p", "rb"))
cOPN = pickle.load(open("Datasets/models/cOPN.p", "rb"))
vectorizer_31 = pickle.load(open("Datasets/models/vectorizer_31.p", "rb"))
vectorizer_30 = pickle.load(open("Datasets/models/vectorizer_30.p", "rb"))

aggregated_text = read_csv("harry_potter_all_character_full_sentence.csv", sep=",", lineterminator='\n')

file_header = ['Character', 'EXT', 'NEU', 'AGR', 'CON', 'OPN']
csv_rows = []



def predict_personality(_text):
    sentences = re.split("(?<=[.!?]) +", text)
    text_vector_31 = vectorizer_31.transform(sentences)
    text_vector_30 = vectorizer_30.transform(sentences)
    EXT = cEXT.predict(text_vector_31)
    NEU = cNEU.predict(text_vector_30)
    AGR = cAGR.predict(text_vector_31)
    CON = cCON.predict(text_vector_31)
    OPN = cOPN.predict(text_vector_31)
    return [EXT[0], NEU[0], AGR[0], CON[0], OPN[0]]


for i in range(len(aggregated_text)):
    text = aggregated_text.iloc[i, 1]
    predictions = predict_personality(text)
    csv_row = [aggregated_text.iloc[i, 0], predictions[0], predictions[1], predictions[2], predictions[3], predictions[4]]
    csv_rows.append(csv_row)
    print(predictions)

with open('aggregated_personality.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(file_header)
    writer.writerows(csv_rows)


# df = pd.DataFrame(dict(r=predictions, theta=['EXT', 'NEU', 'AGR', 'CON', 'OPN']))
# fig = px.line_polar(df, r='r', theta='theta', line_close=True)
# fig.show()
