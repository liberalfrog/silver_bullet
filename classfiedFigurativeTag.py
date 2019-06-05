import fastText as ft
import gensim
import sys
import json
import os

def readTagData(path):
    if os.path.isfile(path):
        with open(path, 'r') as f:
            ys = json.loads(f.read(),encoding='utf-8')
    else:
        with open(path, 'w') as f:
            print("make json file:"+path)
            ys={}
            json.dump(ys,f,indent=4,ensure_ascii=False)


    return ys


#別れた文字列に近い文字を持ってくる
def classfiedFigure(splitedWords):
    print(splitedWords)
    model = gensim.models.KeyedVectors.load_word2vec_format('ja.text8.model.vec')
    wordDic={}
    for word in splitedWords.split():
        wordDic[word] = model.most_similar(word)
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
def makeFigureTag(setWordsList):
    path="figureTag.json"
    ys = readTagData(path)
    #print(ys)
    #fw = open("figureTag.json", 'w')
    for setWords in setWordsList: 
        addDic = classfiedFigure(setWords)
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
        makeFigureTag(sys.argv[2:])
        print("call -t")
    if sys.argv[1]=="-o":
        readTagData(sys.argv[2])
