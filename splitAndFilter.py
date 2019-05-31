from janome.tokenizer import Tokenizer
import sys

def splitWord(sp):
    t = Tokenizer()
    st = sp
    splited=""
    for token in t.tokenize(st):
        hinshi = token.part_of_speech.split(',')[0]
        if hinshi == "形容詞" or hinshi == "動詞" or hinshi == "名詞":
            splited+=token.surface
            splited+=" "
    return splited

if __name__ == '__main__':

    print(splitWord(sys.argv[1]))

