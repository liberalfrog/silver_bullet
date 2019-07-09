def trainFigTagModel(model = 'cbow'):
    import fasttext

    #model = fasttext.train_unsupervised('datas/testFigureLabelData.txt', model=model)
    #model.save_model(t+".vec")
    acc = 100
    headName = "Fig"

    print(timeStamp(headName,acc))



def timeStamp(headName,acc):
    import time
    import datetime
    today = datetime.datetime.fromtimestamp(time.time())
    t = today.strftime('%Y_%m_%d_%H_%M')
    modelName = headName+"_"+str(acc)+"_"+t+".vec"
    return modelName
