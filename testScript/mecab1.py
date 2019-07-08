import MeCab

def get_token(content):
    tokens = []
    tagger = MeCab.Tagger('')
    tagger.parse('')
    node = tagger.parseToNode(content)
    while node:
        tokens.append(node.surface)
        node = node.next
    return tokens

def main():
    content="これはテストコーパスです。これをうまく分割できるかな？"
    print(get_token(content))

if __name__ == '__main__':
    main()
