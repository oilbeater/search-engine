#"-*- coding: utf-8 -*-" 
import jieba
import re
from TextPareser import *

TitleIndex = {}
HxIndex = {}
PIndex = {}

def BuildIndex(text,indexlist):
    #text.
    SegList = jieba.cut_for_search(text)
    for KeyWord in SegList:
        #print KeyWord
        TitleIndex[KeyWord] = []
        for index in re.finditer(KeyWord , text):
            #print index.start()
            TitleIndex[KeyWord].append(index.start())
    pass

#seg = BuildIndex("the english is good",TitleIndex)

rf = open(str(1),'r')
text =  unicode(rf.read(),'utf-8')

TitleText = findTitle(text)
HxText = findHx(text)
PText = findP(text)

for x in TitleText:
    BuildIndex(x,TitleIndex)
for x in HxText:
    BuildIndex(x[1],HxIndex)
for x in PText:
    BuildIndex(x,PIndex)
rf.close()