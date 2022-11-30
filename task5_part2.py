import pickle
import re
import csv
from pandas import *
import string


cEXT = pickle.load(open("Datasets/models/cEXT.p", "rb"))
cNEU = pickle.load(open("Datasets/models/cNEU.p", "rb"))
cAGR = pickle.load(open("Datasets/models/cAGR.p", "rb"))
cCON = pickle.load(open("Datasets/models/cCON.p", "rb"))
cOPN = pickle.load(open("Datasets/models/cOPN.p", "rb"))
vectorizer_31 = pickle.load(open("Datasets/models/vectorizer_31.p", "rb"))
vectorizer_30 = pickle.load(open("Datasets/models/vectorizer_30.p", "rb"))


def predict_personality(text):
    sentences = re.split("(?<=[.!?]) +", text)
    text_vector_31 = vectorizer_31.transform(sentences)
    text_vector_30 = vectorizer_30.transform(sentences)
    EXT = cEXT.predict(text_vector_31)
    NEU = cNEU.predict(text_vector_30)
    AGR = cAGR.predict(text_vector_31)
    CON = cCON.predict(text_vector_31)
    OPN = cOPN.predict(text_vector_31)
    return [EXT[0], NEU[0], AGR[0], CON[0], OPN[0]]


data = read_csv("Results/harry_potter_all_character_full_sentence.csv", sep=",")
csv_header = ['Character', 'EXT', 'NEU', 'AGR', 'CON', 'OPN', 'Sentence']
csv_rows =[]
for i in data.index:
    key = data['Character'][i]
    value = data['Sentence'][i]
    split_sentences_list = value.split("|")


    for sentence in split_sentences_list:
        predictions = predict_personality(sentence.lower().translate(str.maketrans('', '', string.punctuation)))
        csv_row = []
        csv_row.append(key)
        csv_row.append(predictions[0])
        csv_row.append(predictions[1])
        csv_row.append(predictions[2])
        csv_row.append(predictions[3])
        csv_row.append(predictions[4])
        csv_row.append(sentence)
        csv_rows.append(csv_row)


        # print("predicted personality:", predictions[0])

with open('Results/harry_potter_all_sentences_with_personality_characterise.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f, delimiter=';')
    writer.writerow(csv_header)
    writer.writerows(csv_rows)

