if __name__=="__main__":
    import scripts.fromSubjectToSuitImage as fr
    import sys
    if sys.argv[1]=="-t":
        fr.setImageDataJson(sys.argv[2],sys.argv[3:])
