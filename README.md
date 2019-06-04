# silver_bullet

# Overview
タイトルを入れると予め作成されたモデルとタグ群を使い、タグを複数持つ画像群から近いものをひっぱてくるpythonでの関数です。

入力例

「焼き肉をみんなで食べに行きましょう」

出力例

一番目一致率の高い画像のパス

二番目一致率の高い画像のパス

…

指定の数の画像

学習用に作っているので完成度は低いし、まだまだ未完成ですがこれから実装をしていきます。
# Description
silver_bulletは文章の分析を２つのタグに分け、fast_textで作ったword2vecのモデルを使いつつ柔軟に適切なタグの画像を探します。

具象タグ

「焼き肉」、「みんな」、「同窓会」、「米」

比較的具体的なが多く、タグを事前に事象タグのリストに登録しておけば追加したタイミングで使えます。

抽象タグ

「楽しい」、「わくわく」、「こわい」

抽象タグは事前にタグでラベル付けしたデータセットを用意し、それをfasttextでラベル付けのモデルを作成する。それを元にタイトル全体をラベル付けして、それの割合を元にタグを取り出します。

# Requirement
python3（できるだけ最近のものでローカルでは3.7.0で行った）

Janome==0.3.9

gensim==3.7.3

fasttextを自分でpipビルドしてください。

fasttextで学習済みの単語モデルと抽象タグをラベル付けできるモデル
# Usage

タイトルに適した画像パスとタグを返します。

python  fromSubjectToSuitImage.py -c　タイトル

画像パスとタグの組み合わせを登録する。

python  fromSubjectToSuitImage.py -t imagePath tag1 tag2 tag3 tag4

tag1 tag2 tag3を登録

python  classfiedFigurativeTag.py -t tag1 tag2 tag3　
