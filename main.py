from pandas import *


def read_data():
    corpus = {}
    data = read_csv("Datasets/Harry Potter 1.csv", sep=";")
    print(data)
    print(data['Character'].unique())
    # data['Character'] = data['Character'].str.rstrip()
    # print(data.Character.unique())
    data['Character'] = data['Character'].str.replace(" ", "")
    # data['Character'] = data['Character'].str.replace("\xa0", "")
    print(data.Character.tolist())

    # corpus['Dumbledore'] = data['Sentence'][0] + data['Sentence'][3]

    for i in data.index:
        key = data['Character'][i]
        if key in corpus.keys():
            corpus[key] = corpus[key] + ' ' + data['Sentence'][i]
        else:
            corpus[key] = data['Sentence'][i]
    print(corpus)
    print('\n\n')
    print(corpus['McGonagall'])
    corpus_df = DataFrame.from_dict(corpus, orient='index', columns=['Vocabulary'])

    # print(corpus_df['Dumbledore'])
    corpus_df.to_csv('test.csv', sep=';')

    corpus['newKey'] = "value of new key"


def main():
    read_data()


if __name__ == "__main__":
    main()
