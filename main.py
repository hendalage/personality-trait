from pandas import *


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

    print(corpus)

    # corpus_df = DataFrame.from_dict(corpus, orient='index', columns=['Vocabulary'])


def main():
    read_data()


if __name__ == "__main__":
    main()
