#!/usr/bin/python

from konlpy.tag import Kkma
from konlpy.tag import Mecab; m = Mecab()
from glob import glob


def readtxt(filename, encoding='utf-8'):
    with open(filename, 'r') as f:
        return f.read().decode(encoding)


def tokenize(filename):
    d = readtxt(filename)
    sentences = kkma.sentences(d)
    str_list = []
    for sentence in sentences:
        pos = m.pos(sentence)
        filtered = filter(lambda x: not (x[1].startswith('J') or x[1].startswith('S')
                                         or x[1].endswith('EF')
                                         or x[1].startswith('XS') or x[1].startswith('EC')
                                         or x[1].endswith('ETM')
                                         or x[1].startswith('IC')), pos)
        # filtered = filter(lambda x: len(x[0])>1, filtered)
        text = ' '.join(p[0] for p in filtered)
        # poss = '\n '.join(','.join(pp) for pp in pos)
        str_list.append(text)

    textall = '\n'.join(str_list)
    year = filename.split('/')[-1].split('.')[0]
    with open('../data/%s_tokenized.txt' % year, 'w') as f:
        f.write(textall.encode('utf-8'))


kkma = Kkma()
filenames = glob('../data/*.txt')
for filename in filenames:
    print filename
    tokenize(filename)
