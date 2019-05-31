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
    #print(wordDic.values())
    usedKeys=[]
    for tK in tagsDic.keys():
        for wK in wordDic.keys():
            if tK==wK:
                usedKeys.append((tK,1))

    for tK in tagsDic.keys():
        for wK in wordDic.values():
            for pK in wK:
                if tK==pK[0]:
                    usedKeys.append(pK)
    return usedKeys


#画像の具象的なタグの一覧をjsonファイルで保存する関数
def makeFigureTag(s):
    p=""
    with open("figureTag.json", 'r') as f:
        ys = json.loads(f.read(),encoding='utf-8')
    print(ys)
    #fw = open("figureTag.json", 'w')
    addDic = classfiedFigure(s)
    ys.update(addDic)
    with open("figureTag.json",'w',encoding='utf-8') as f:
        json.dump(ys,f,indent=4,ensure_ascii=False)


if __name__== "__main__":
    #-sを渡すことでタグを探してくる
    if sys.argv[1]=="-s":
        print(searchSuitTag(sys.argv[2]))
        print("call -s")
    #-tを渡すことでタグの登録
    if sys.argv[1]=="-t":
        makeFigureTag(sys.argv[2])
        print("call -t")
