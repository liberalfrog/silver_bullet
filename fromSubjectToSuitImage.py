import sys
import splitAndFilter
import classfiedAbstractTag as ab
import classfiedFigurativeTag as fig
import json

#画像データは辞書で画像がキーでタグのリストがバリュー
def setImageDataJson(imagePath,tags):
    p=""
    path="imagesData.json"

    with open(path, 'r') as f:
        savedTags = json.loads(f.read(),encoding='utf-8')

    addDic = {imagePath:tags}
    savedTags.update(addDic)

    with open(path,'w',encoding='utf-8') as f:
        json.dump(savedTags,f,indent=4,ensure_ascii=False)


def fromSubjectToImagePath(subjectStr):
    splitedSub=splitAndFilter.splitWord(subjectStr)

    imagePath="imagesData.json"
    matchTagList = []
    matchDic={}
    savedTags={}

    figTag=fig.searchSuitTag(splitedSub)
    absTag=ab.classfiedAbsTag(splitedSub)

    usedTags =figTag + absTag

    with open(imagePath, 'r') as f:
        savedTags = json.loads(f.read(),encoding='utf-8')

    for tagKey,tagValue in savedTags.items():
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

    for num in range(2):
        print(matchDic[matchTagList[num]])
        pass


if  __name__=="__main__":

    if sys.argv[1]=="-c":
        fromSubjectToImagePath(sys.argv[2])

    elif sys.argv[1]=="-t":
        setImageDataJson(sys.argv[2],sys.argv[3:])
    else:
        print("wrong syntax")

