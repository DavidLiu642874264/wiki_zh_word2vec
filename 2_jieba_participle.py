#!/usr/bin/env python
# -*- coding: utf-8  -*-
# 逐行读取文件数据进行jieba分词

import jieba
import jieba.analyse
import jieba.posseg as pseg # 引入词性标注接口
import codecs
import sys


if __name__ == '__main__':
    f = codecs.open('wiki.zh.simp.txt', 'r', encoding='utf8')
    target = codecs.open('wiki.zh.simp.seg.txt', 'w', encoding='utf8')
    print('open files.')

    line_num = 1
    line = f.readline()
    while line:
        if line_num % 10000 == 0:
            print('---processing ', line_num,' article---', line)
        seg_list = jieba.cut(line, cut_all=False)
        line_seg = ' '.join(seg_list)
        target.writelines(line_seg)
        line_num += 1
        line = f.readline()

    print('well done.')
    f.close()
    target.close()
