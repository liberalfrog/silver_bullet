def splitWord(sp):
    import sys
    import MeCab

    m = MeCab.Tagger ("-Ochasen")
    node = m.parseToNode(sp)
    splited = ""

    while node:
        #単語を取得
        word = node.surface
        #品詞を取得
        hinshi = node.feature.split(",")[0]
        if hinshi == "形容詞" or hinshi == "動詞" or hinshi == "名詞":
            splited+=node.surface
            splited+=" "
        #次の単語に進める
        node = node.next
    return splited

if __name__ == '__main__':
    import sys
    f = open(sys.argv[1])
    data1 = f.read()  # ファイル終端まで全て読んだデータを返す
    f.close()
    print(data1)
    print(splitWord(data1))
