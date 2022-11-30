import csv
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from pandas import *


data = read_csv("Results/harry_potter_all_sentences_with_personality.csv", sep=";")

data_rows = []
file_header = ['Character', 'Sentence', 'Negative', 'Neutral', 'Positive', 'Compound',
               'EXT_Pos', 'EXT_Neg',
               'NEU_Pos', 'NEU_Neg',
               'AGR_Pos', 'AGR_Neg',
               'CON_Pos', 'CON_Neg',
               'OPN_Pos', 'OPN_Neg']

analyzer = SentimentIntensityAnalyzer()

progress = 0

for index, row in data.iterrows():
    sentence = row['Sentence']
    character = row['Character']
    _EXT = row['EXT']
    _NEU = row['NEU']
    _AGR = row['AGR']
    _CON = row['CON']
    _OPN = row['OPN']

    output_row: list = []

    vs = analyzer.polarity_scores(sentence)

    output_row.append(character)
    output_row.append(sentence)

    compound_sentiment = vs['compound']

    output_row.append(vs['neg'])
    output_row.append(vs['neu'])
    output_row.append(vs['pos'])
    output_row.append(compound_sentiment)

    if compound_sentiment >= 0:
        if _EXT:
            output_row.append(1)
            output_row.append(0)
        else:
            output_row.append(0)
            output_row.append(0)
        if _NEU:
            output_row.append(1)
            output_row.append(0)
        else:
            output_row.append(0)
            output_row.append(0)
        if _AGR:
            output_row.append(1)
            output_row.append(0)
        else:
            output_row.append(0)
            output_row.append(0)
        if _CON:
            output_row.append(1)
            output_row.append(0)
        else:
            output_row.append(0)
            output_row.append(0)
        if _OPN:
            output_row.append(1)
            output_row.append(0)
        else:
            output_row.append(0)
            output_row.append(0)
    else:
        if _EXT:
            output_row.append(0)
            output_row.append(1)
        else:
            output_row.append(0)
            output_row.append(0)
        if _NEU:
            output_row.append(0)
            output_row.append(1)
        else:
            output_row.append(0)
            output_row.append(0)
        if _AGR:
            output_row.append(0)
            output_row.append(1)
        else:
            output_row.append(0)
            output_row.append(0)
        if _CON:
            output_row.append(0)
            output_row.append(1)
        else:
            output_row.append(0)
            output_row.append(0)
        if _OPN:
            output_row.append(0)
            output_row.append(1)
        else:
            output_row.append(0)
            output_row.append(0)

    data_rows.append(output_row)
    data_row = []
    progress += 1
    print(progress)

with open('sentiments.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(file_header)
    writer.writerows(data_rows)


"""
Summarise data for plotting
"""
summary_file_header = ['Character',
                       'EXT_Pos', 'EXT_Neg',
                       'NEU_Pos', 'NEU_Neg',
                       'AGR_Pos', 'AGR_Neg',
                       'CON_Pos', 'CON_Neg',
                       'OPN_Pos', 'OPN_Neg']

sentiment_data = read_csv("sentiments.csv", sep=",")

summary_data_rows = []
previous_character = sentiment_data['Character'].tolist()[0]

temp_row = ["temp", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for _index, _row in sentiment_data.iterrows():
    if previous_character == _row['Character']:
        temp_row[0] = _row['Character']
        temp_row[1] = temp_row[1] + _row['EXT_Pos']
        temp_row[2] = temp_row[2] + _row['EXT_Neg']
        temp_row[3] = temp_row[3] + _row['NEU_Pos']
        temp_row[4] = temp_row[4] + _row['NEU_Neg']
        temp_row[5] = temp_row[5] + _row['AGR_Pos']
        temp_row[6] = temp_row[6] + _row['AGR_Neg']
        temp_row[7] = temp_row[7] + _row['CON_Pos']
        temp_row[8] = temp_row[8] + _row['CON_Neg']
        temp_row[9] = temp_row[9] + _row['OPN_Pos']
        temp_row[10] = temp_row[10] + _row['OPN_Neg']
    else:
        summary_data_rows.append(temp_row)
        temp_row = ["temp", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        previous_character = _row['Character']
        temp_row[0] = _row['Character']
        temp_row[1] = temp_row[1] + _row['EXT_Pos']
        temp_row[2] = temp_row[2] + _row['EXT_Neg']
        temp_row[3] = temp_row[3] + _row['NEU_Pos']
        temp_row[4] = temp_row[4] + _row['NEU_Neg']
        temp_row[5] = temp_row[5] + _row['AGR_Pos']
        temp_row[6] = temp_row[6] + _row['AGR_Neg']
        temp_row[7] = temp_row[7] + _row['CON_Pos']
        temp_row[8] = temp_row[8] + _row['CON_Neg']
        temp_row[9] = temp_row[9] + _row['OPN_Pos']
        temp_row[10] = temp_row[10] + _row['OPN_Neg']

summary_data_rows.append(temp_row)

with open('Results/sentiment_summery.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(summary_file_header)
    writer.writerows(summary_data_rows)

for each_row in summary_data_rows:
    print(each_row)
