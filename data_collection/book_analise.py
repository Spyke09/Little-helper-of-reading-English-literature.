from data_collection import data_base
import nltk
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer


# рабочий файл с набросками того, что должно быть по итогу

# функция-генератор для чтения файла
def words_gen(st: str):
    f = open(fr'data_collection\set of words\{st}', 'r')
    while 1:
        a = f.readline()
        if not a:
            break
        a = a.replace("\n", '')
        yield a
    f.close()


# прототип функции words_distribution из analise.py
def get_dict_dict(st):
    f = open(fr'data_collection\set of words\{st}')
    tokenizer = nltk.RegexpTokenizer(r'\w+')
    snow_stemmer = SnowballStemmer(language='english')
    s = dict()
    length = 0
    stopWords = set(stopwords.words('english'))
    while 1:
        try:
            a = f.readline()
        except:
            continue
        if not a:
            break
        a = tokenizer.tokenize(a.lower())
        for j in a:
            i = snow_stemmer.stem(j)
            if i not in stopWords:
                length += 1
                if i not in s:
                    s[i] = 1.0
                else:
                    s[i] += 1.0

    temp = []
    for i in s.keys():
        if not data_base.translate(i):
            length -= s[i]
            temp.append(i)

    for i in temp:
        s.pop(i)
    s = sort_dict(s)

    for i in s.keys():
        s[i] /= length
    f.close()
    return s


# отсортировывает словарь по значению
def sort_dict(d):
    res = dict()
    so = sorted(d, key=d.get)
    for i in so:
        res[i] = d[i]
    return res


# прототипы функций сложности
def difficult1(input_set: dict):
    temp = input_set.copy()
    for i in words_gen("most common.txt"):
        if i in temp:
            temp.pop(i)
    return sum(temp.values()) * 100


def difficult2(input_set: dict):
    len_n = len(input_set)
    temp = input_set.copy()
    for i in words_gen("most common.txt"):
        if i in temp:
            temp.pop(i)
    return (len_n - len(temp)) / len_n
