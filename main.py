import statistics
import csv
from pandas import *
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string

# Uncomment this when running for the first time
import nltk
nltk.download('stopwords')
nltk.download('punkt')


def read_data():
    corpus = {}
    occurrence_list = {}

    data = read_csv("Datasets/Harry Potter 3.csv", sep=";")
    # print(data)
    # print(data['Character'].unique())

    data['Character'] = data['Character'].str.replace(" ", "")
    # print(data.Character.tolist())
    st_deviation_data_array = []
    csv_rows = []

    for i in data.index:
        key = data['Character'][i]
        st_deviation_data_array.append(len(data['Sentence'][i].lower()
                                           .translate(str.maketrans('', '', string.punctuation)).split()))
        if key in corpus.keys():
            corpus[key] = corpus[key] + ' ' + data['Sentence'][i]
            occurrence_list[key] = occurrence_list[key] + 1
        else:
            corpus[key] = data['Sentence'][i]
            occurrence_list[key] = 1

    for character in corpus.keys():
        # print(character)
        new_sentence = corpus[character].lower().translate(str.maketrans('', '', string.punctuation))
        # print(new_sentence)
    # print(corpus)
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

        csv_row = []
        csv_row.append(character)
        csv_row.append(word_tokens_count)
        csv_row.append(size_of_vocab)
        csv_row.append(avg_len_of_script)
        csv_row.append(prop_of_stop_word)
        csv_rows.append(csv_row)

    file_header = ['Character', 'Tokens', 'Size_of_vocab', 'Avg_length', 'Prop_stop_word']

    standard_deviation = statistics.stdev(st_deviation_data_array)
    print(standard_deviation)

    with open('new_harry_potter_3_analysis.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(file_header)
        writer.writerows(csv_rows)

    # corpus_df = DataFrame.from_dict(corpus, orient='index', columns=['Vocabulary'])


def main():
    read_data()


if __name__ == "__main__":
    main()
