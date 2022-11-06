import pickle
# from sklearn.feature_extraction.text import CountVectorizer
import plotly.express as px
import re
import csv
from pandas import *


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


# data = read_csv("Datasets/Harry Potter 1.csv", sep=";")
# data = read_csv("harry_potter_all_character_full_sentence.csv", sep=";")
data = read_csv("harry_potter_all_sentences_with_personality.csv", sep=";")
# data = read_csv("harry_potter_all_character_full_sentence_with_breakpoints.csv", sep=";")
csv_header = ['Character', 'EXT', 'NEU', 'AGR', 'CON', 'OPN', 'EXT_MEAN', 'NEU_MEAN', 'AGR_MEAN', 'CON_MEAN', 'OPN_MEAN', 'Type']
csv_rows =[]
sentence_count = 0
current_character = ''

ext_tot = 0
neu_tot = 0
agr_tot = 0
con_tot = 0
opn_tot = 0

for i in data.index:
    key = data['Character'][i]
    value = data['Sentence'][i]
    ext = data['EXT'][i]
    neu = data['NEU'][i]
    agr = data['AGR'][i]
    con = data['CON'][i]
    opn = data['OPN'][i]
    csv_row = []

    if current_character == '':
        current_character = key

    if key == current_character:

        sentence_count = sentence_count + 1
        ext_tot = ext_tot + ext
        neu_tot = neu_tot + neu
        agr_tot = agr_tot + agr
        con_tot = con_tot + con
        opn_tot = opn_tot + opn
    else:

        if sentence_count == 0:
            sentence_count = 1

        ext_tot = ext_tot / sentence_count
        neu_tot = neu_tot / sentence_count
        agr_tot = agr_tot / sentence_count
        con_tot = con_tot / sentence_count
        opn_tot = opn_tot / sentence_count

        pred_values = []
        csv_row.append(current_character)

        csv_row.append(ext_tot)
        csv_row.append(neu_tot)
        csv_row.append(agr_tot)
        csv_row.append(con_tot)
        csv_row.append(opn_tot)

        pred_values.append(ext_tot)
        pred_values.append(neu_tot)
        pred_values.append(agr_tot)
        pred_values.append(con_tot)
        pred_values.append(opn_tot)

        max_value = max(pred_values)
        type_of_personality = ''

        if ext_tot == max_value:
            csv_row.append(1)
            type_of_personality = "EXT"
        else:
            csv_row.append(0)

        if neu_tot == max_value:
            csv_row.append(1)
            type_of_personality = "NEU"
        else:
            csv_row.append(0)

        if agr_tot == max_value:
            csv_row.append(1)
            type_of_personality = "AGR"
        else:
            csv_row.append(0)

        if con_tot == max_value:
            csv_row.append(1)
            type_of_personality = "CON"
        else:
            csv_row.append(0)

        if opn_tot == max_value:
            csv_row.append(1)
            type_of_personality = "OPN"
        else:
            csv_row.append(0)

        ext_tot = 0
        neu_tot = 0
        agr_tot = 0
        con_tot = 0
        opn_tot = 0
        csv_row.append(type_of_personality)
        sentence_count = 0
        csv_rows.append(csv_row)
        current_character = key






    # split_sentences_list = value.split("|")


    # for sentence in split_sentences_list:
    #     predictions = predict_personality(sentence)
    #     csv_row = []
    #     csv_row.append(key)
    #     csv_row.append(predictions[0])
    #     csv_row.append(predictions[1])
    #     csv_row.append(predictions[2])
    #     csv_row.append(predictions[3])
    #     csv_row.append(predictions[4])
    #     csv_row.append(sentence)
    #     csv_rows.append(csv_row)


        # print("predicted personality:", predictions[0])

# with open('harry_potter_all_sentences_with_personality_characterise.csv', 'w', encoding='UTF8', newline='') as f:
with open('harry_potter_median_personality.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f, delimiter=';')
    writer.writerow(csv_header)
    writer.writerows(csv_rows)
# df = DataFrame(dict(r=predictions, theta=['EXT', 'NEU', 'AGR', 'CON', 'OPN']))
# fig = px.line_polar(df, r='r', theta='theta', line_close=True)
# fig.show()
