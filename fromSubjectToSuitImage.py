import sys
import splitAndFilter
import classfiedAbstractTag as ab
import classfiedFigurativeTag as fig
import json

#画像データは辞書で画像がキーでタグのリストがバリュー
def setImageJson(imagePath,tag1,tag2,tag3,tag4):
    p=""
    path="imagesData.json"
    with open(path, 'r') as f:
        ys = json.loads(f.read(),encoding='utf-8')
    #fw = open(path, 'w')
    #ys={}
    addDic = {imagePath:[tag1,tag2,tag3,tag4]}
    ys.update(addDic)
    with open(path,'w',encoding='utf-8') as f:
        json.dump(ys,f,indent=4,ensure_ascii=False)

def fromSubjectToSuitImage(s):
    s=splitAndFilter.splitWord(sys.argv[2])
    path="imagesData.json"
    #print(s)
    figTag=fig.searchSuitTag(s)
    absTag=ab.classfiedAbsTag(s)
    #print(figTag)
    #print(absTag)
    usedTags =figTag + absTag
    ys={}
    with open(path, 'r') as f:
        ys = json.loads(f.read(),encoding='utf-8')
    matchTagList = []
    matchDic={}

    for tagKey,tagValue in ys.items():
        tagSum = 0
        for t in tagValue:
            for usedKey in usedTags:
                if t ==usedKey[0]:
                    #print(tagKey)
                    tagSum+=usedKey[1]
        matchTagList.append(tagSum)
        matchDic[tagSum]=tagKey
    
    matchTagList = sorted(matchTagList)
    matchTagList.reverse()
    #print(matchTagList)
    #print(matchDic)
    for num in range(2):
        print(matchDic[matchTagList[num]])
        pass
    


if  __name__=="__main__":

    if sys.argv[1]=="-s":
        fromSubjectToSuitImage(sys.argv[2])

    elif sys.argv[1]=="-t":
        setImageJson(sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5],sys.argv[6])
    else:
        print("wrong syntax")

