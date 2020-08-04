__author__ = 'david.liu'
# -*- coding: utf-8  -*-

import codecs


if __name__ == '__main__':
    f = codecs.open('wiki.zh.simp.seg.txt', 'r', encoding='utf8')
    print('open files.')

    line_num = 1
    line = f.readline()
    while line:
        if line_num % 10000 == 0:
            print('---reading ', line_num,' article seg---', line)
        line_num += 1
        line = f.readline()

    print('well done.')
    f.close()
