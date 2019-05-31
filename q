import fastText as ft
import gensim
import sys
import json

#別れた文字列に近い文字を持ってくる
def classfiedFigure(s):
    m = gensim.models.KeyedVectors.load_word2vec_format('ja.text8.model.vec')
    wordDic={}
    for sa in s.split():
        wordDic[sa] = m.most_similar(sa)
    return wordDic

#別れたタグに近い文字列をさがす
def searchSuitTag(s):
    wordDic = classfiedFigure(s)
    size=10
    tagsDic=""
    with open("figureTag.json", 'r') as f:
         tagsDic= json.loads(f.read(),encoding='utf-8')
    print(tagsDic.keys())
    print(wordDic.values())
    usedKeys=[]
    for tK in tagsDic.keys():
        for wK in wordDic.keys():
            if tK==wK:
                usedKeys.append((tK,1))

    for tK in tagsDic.keys():
        for wK in wordDic.values():
            for pK in wK:
                print(pK[0])
                if tK==pK[0]:
                    usedKeys.append(pK)
    print(usedKeys)


#画像の具象的なタグの一覧をjsonファイルで保存する関数
def makeFigureTag(s):
    p=""
    with open("figureTag.json", 'r') as f:
        p = json.loads(f.read(),encoding='utf-8')
    print(p)
    #fw = open("figureTag.json", 'w')
    ys = classfiedFigure(s)
    with open("figureTag.json",'w',encoding='utf-8') as f:
        json.dump(ys,f,indent=4,ensure_ascii=False)


if __name__== "__main__":
    if sys.argv=="-s":
        print(searchSuitTag(sys.argv[2]))
    if sys.argv=="-t"
        makeFigureTag(sys.argv[2])
