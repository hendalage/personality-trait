from pandas import *
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Uncomment this when running for the first time
# import nltk
# nltk.download('stopwords')
# nltk.download('punkt')


def read_data():
    corpus = {}

    data = read_csv("Datasets/Harry Potter 1.csv", sep=";")
    print(data)
    print(data['Character'].unique())

    data['Character'] = data['Character'].str.replace(" ", "")
    print(data.Character.tolist())

    for i in data.index:
        key = data['Character'][i]
        if key in corpus.keys():
            corpus[key] = corpus[key] + ' ' + data['Sentence'][i]
        else:
            corpus[key] = data['Sentence'][i]

    # print(corpus)
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(corpus['Dumbledore'])
    # filtered_sentence = [w for w in word_tokens if not w.lower() in stop_words]
    filtered_sentence = []

    for w in word_tokens:
        if w not in stop_words:
            filtered_sentence.append(w)

    print(word_tokens)
    print(filtered_sentence)

    # corpus_df = DataFrame.from_dict(corpus, orient='index', columns=['Vocabulary'])


def main():
    read_data()


if __name__ == "__main__":
    main()
