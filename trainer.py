if __name__ =='__main__':
    import sys

    if(sys.argv[1]=='-f'):
        import scripts.trainFigTagModel as tft
        tft.trainFigTagModel()

    elif(sys.argv[1]=='-a'):
        import scripts.trainAbsTagModel as tat

