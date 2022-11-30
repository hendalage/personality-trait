import math
import statistics
import csv
from pandas import *
from numpy import dot
from numpy.linalg import norm

data = read_csv("harry_potter_all_sentences_with_personality.csv", sep=";")
data_all_char = read_csv("harry_potter_median_personality.csv", sep=";")

csv_header = ['Character', 'EXT', 'NEU', 'AGR', 'CON', 'OPN', 'Cosine', 'Sentence']
csv_rows = []

ind = 0
result_array = []
current_character = ''

for i in data.index:
    character = data['Character'][i]
    csv_row = []
    csv_row.append(data['Character'][i])
    csv_row.append(data['EXT'][i])
    csv_row.append(data['NEU'][i])
    csv_row.append(data['AGR'][i])
    csv_row.append(data['CON'][i])
    csv_row.append(data['OPN'][i])

    if current_character != character:
        for index_of_character in data_all_char.index:
            if data_all_char['Character'][index_of_character] == character:
                ind = index_of_character
                current_character = character
                break

    row = [data['EXT'][i], data['NEU'][i], data['AGR'][i], data['CON'][i], data['OPN'][i]]
    character_personality = [data_all_char['EXT_MEAN'][ind], data_all_char['NEU_MEAN'][ind],
                             data_all_char['AGR_MEAN'][ind], data_all_char['CON_MEAN'][ind],
                             data_all_char['OPN_MEAN'][ind]]

    result = dot(row, character_personality) / (norm(row) * norm(character_personality))


    csv_row.append(result)
    csv_row.append(data['Sentence'][i])
    if not (math.isnan(result)):
        result_array.append(result)
    csv_rows.append(csv_row)

standard_deviation = statistics.stdev(result_array, 1)
print(standard_deviation)
# 0.10456028641888981

with open('harry_potter_all_sentences_with_cosine.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f, delimiter=';')
    writer.writerow(csv_header)
    writer.writerows(csv_rows)
