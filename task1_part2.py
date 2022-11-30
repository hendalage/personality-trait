import statistics
import csv
from pandas import *
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string

import nltk
nltk.download('stopwords')
nltk.download('punkt')


def read_data():
    corpus = {}
    occurrence_list = {}

    data = read_csv("Datasets/Harry Potter 1.csv", sep=";")
    hp2 = read_csv("Datasets/Harry Potter 2.csv", sep=";")
    hp3 = read_csv("Datasets/Harry Potter 3.csv", sep=";")

    data = data.append(hp2, ignore_index=True)
    data = data.append(hp3, ignore_index=True)

    data['Character'] = data['Character'].str.strip()
    data['Character'] = data['Character'].str.lower()
    st_deviation_data_array = []
    csv_rows = []

    for i in data.index:
        key = data['Character'][i]
        st_deviation_data_array.append(len(data['Sentence'][i].lower().split()))
        if key in corpus.keys():
            corpus[key] = corpus[key] + ' ' + data['Sentence'][i].lower().translate(str.maketrans('', '', string.punctuation))

            occurrence_list[key] = occurrence_list[key] + 1
        else:
            corpus[key] = data['Sentence'][i].lower().translate(str.maketrans('', '', string.punctuation))

            occurrence_list[key] = 1

    for character in corpus.keys():
        new_sentence = corpus[character]
        stop_words = set(stopwords.words('english'))
        word_tokens = word_tokenize(new_sentence)
        word_tokens_count = len(word_tokens)

        filtered_sentence = []
        for w in word_tokens:
            if w not in stop_words:
                filtered_sentence.append(w)

        size_of_vocab = len(filtered_sentence)

        avg_len_of_script = len(new_sentence.split()) / occurrence_list[character]

        prop_of_stop_word = (size_of_vocab * 100) / len(new_sentence.split())

        csv_row = [character, new_sentence, word_tokens_count, avg_len_of_script, prop_of_stop_word]
        csv_rows.append(csv_row)

    file_header = ['Character', 'Tokens', 'Size_of_vocab', 'Avg_length', 'Prop_stop_word']

    standard_deviation = statistics.stdev(st_deviation_data_array)
    print(standard_deviation)

    with open('Results/harry_potter_all_analysis.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(file_header)
        writer.writerows(csv_rows)


def main():
    read_data()


if __name__ == "__main__":
    main()
