#!/usr/bin/env python
# -*- coding: utf-8  -*-
#测试训练好的模型

import warnings
warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')# 忽略警告
import sys
#import importlib
#importlib.reload(sys)
#reload(sys)
#sys.setdefaultencoding('utf8')
import gensim
import jieba

model =None
def load_model():
    global model
    model = gensim.models.Word2Vec.load(fdir + 'wiki.zh.text.model')
    return model
def calc_similary():
    global model
    line = "中建四局土木工程有限公司深圳分公司"
    words = list(jieba.cut(line))
    word_list =[]
    for w in words:
        if w not in model.wv.vocab:
            print("input word %s not in dict. skip this turn" % w)
        else:
            word_list.append(w)
    candidates = []
    line_list =[u'中建二局基础设施建设投资有限公司南方分公司',u"中建四局土木工程有限公司",u"中建二局土木工程有限公司",u'中建二局土木工程有限公司深圳分公司']
    for line_e in line_list:
        seg_list = jieba.cut(line_e, cut_all=False)
        line_seg = ' '.join(seg_list)
        candidates.append(line_seg.split(' '))
    res = []
    index = 0
    flag = False
    for candidate in candidates:
        for c in candidate:
            if c not in model.wv.vocab:
                print("input word %s not in dict. skip this turn" % w)
                flag = True
        if flag:
            break
        score = model.n_similarity(word_list,candidate)
        resultInfo = {'id':index,"score":score,"text":" ".join(candidate)}
        res.append(resultInfo)
        index +=1
    res.sort(key=lambda x:x['score'],reverse=True)

    for rr in res:
        print(rr)
        print("-"*50)


if __name__ == '__main__':
    #global model
    #fdir = '/Users/sy/Desktop/pyRoot/wiki_zh_vec/'
    fdir = ''
    load_model()

    calc_similary()
    print("start similar")
    word = model.most_similar(u"百度 科技 有限 公司".split(" "),topn=10)
    for t in word:
        print(t[0], t[1])
    print("*"*50)
    word = model.most_similar(u"足球")
    for t in word:
        print(t[0], t[1])
    print("*"*50)
    word = model.most_similar(u"刘备")
    for t in word:
        print(t[0], t[1])
    print("*"*50)
    word = model.most_similar(u"曹操")
    for t in word:
        print(t[0], t[1])
    print("*"*50)
    word = model.most_similar(u"毛泽东")
    for t in word:
        print(t[0], t[1])
    print("*"*50)
    simi = model.similarity(u"毛泽东",u"毛泽东")
    print("similarity:{}".format(simi))
    print("*"*50)
    #simi = model.similarity(u"百度",u"百度科技有限公司")
    #print("similarity:{}".format(simi))
    '''
    line = "中建四局土木工程有限公司深圳分公司"
    seg_list = jieba.cut(line, cut_all=False)
    line_seg = ' '.join(seg_list)
    print("line_seg:{}".format(line_seg))
    line_list =[u'中建二局基础设施建设投资有限公司南方分公司',u"中建四局土木工程有限公司",u"中建二局土木工程有限公司"]
    for line_item in line_list:
        simi = model.similarity(line,line_list)
        print("similarity:{}".format(simi))
    result = model.most_similar(line_seg.split( ' '))#,restrict_vocab=line_list)
    for t in result:
        print(t[0], t[1])

    word = model.most_similar(positive=[u'皇上',u'国王'],negative=[u'皇后'])
    for t in word:
        print t[0],t[1]


    print model.doesnt_match(u'太后 妃子 贵人 贵妃 才人'.split())
    print model.similarity(u'书籍',u'书本')
    print model.similarity(u'逛街',u'书本')
    '''


