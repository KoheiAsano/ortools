# ortools_shiftg

Google Optimization Toolsを使って１０人の従業員を制約条件に基づいて、一週間ずつ確認を取りながら学習してスケジュールを作っていくPythonプログラム

初期設定平日は３人  土日は５人の従業員を配員  
それぞれの従業員は


必要ライブラリのインストール(足りないのがあれば必要に応じてpip installしてください。)
```
$ pip install  -r requirements.txt
```  


# **dic**
---

## ・[news_general_pn.txt](https://github.com/aitokyolab/make_pn_dic/blob/master/definepn/dic/news_general_pn.txt)
ニュース一般名詞(mecab neologd)の極性辞書、時事的成分を含まなく、更新の必要がないものを乗せる。
## ・[news_proper_pn.txt](https://github.com/aitokyolab/make_pn_dic/blob/master/definepn/dic/news_proper_pn.txt)
ニュース固有名詞(mecab neologd)の極性辞書、本プログラムによって更新する。（極性値未定義）
## ・[spet_words.txt](https://github.com/aitokyolab/make_pn_dic/blob/master/definepn/dic/spet_words.txt)
辞書更対象記事から除外する用語集
## ・[stop_words.txt](https://github.com/aitokyolab/make_pn_dic/blob/master/definepn/dic/stop_words.txt)
単語分かちするときに除外する情報量のない単語リスト
## ・intsrc
初期極性辞書のソースとなるCSV、Jupyterプログラム


# **src**
---
## ・[update_propn.py](https://github.com/aitokyolab/make_pn_dic/blob/feature_updpn/definepn/src/update_propn.py)
ウィキペディアフォルダに含まれている約4000テキストとニューステキストに対してTF-IDF値を計算して、上位100位の固有名詞(proper noun)既登録極性語との共起関係を調べ、対象の語と同じ生地に出てくる極性語の平均値を新語の極性値とする。

## 実行例

definepn/  
├ dic/  
│├ news_general_pn.txt  
│├ news_proper_pn.txt  
│├ pn_dic.csv  
│  ppdic  
│├ spet_words.t  
│├ stop_words.t  
│└ inits  
└ src/  
\t  ├wiki_AA_text  
\t  ├((新しいニュースCSVフォルダ)  
\t  ├update_pn.py  
\t  └proccessing_chunk(極性更新プログラムをチャンクごとにわけた)  

```
$ python update_propn.py 02
```


## プログラムの分割(/definepn/src/proccessing_chunk)

1. [exclude_spet.py](https://github.com/aitokyolab/make_pn_dic/blob/feature_tf-idf/definepn/src/exclude_spet.py)
スポーツ、エンタメ、プロモーション記事の削除.更新対象となる記事のみのCSVを出力
2. [extract_new_pronoun.py](https://github.com/aitokyolab/make_pn_dic/blob/feature_tf-idf/definepn/src/extract_new_pronoun.py)
新出固有名詞の抽出、Frequency,TF-IDFの計算
3. [make_pn.py](https://github.com/aitokyolab/make_pn_dic/blob/feature_updpn/definepn/src/update_pro_dic.py)
既存の辞書（1.news_general_pn.txt,2.news_proper_pn.txt,3.pn_dic.csv）共起関係で新固有名詞の極性付け、既存固有名詞の極性更新


各分割プログラム実行方法はそれぞれのファイルのドキュメンテーション文字列参照


# **作業フローの記録**
---
- [x] ニュースフォルダ01_txtを[extract_new_pronoun.py](https://github.com/aitokyolab/make_pn_dic/blob/master/definepn/src/extract_new_pronoun.py)でTF-IDFで抜き出した
- [x] 一般名詞は、漢字ベースで極性付け(jupyterソースはdic/src)、そのあと手修正。固有名詞はGoogleニュースで検索し、上位のものから浅野の主観で極性付け
- [x] 上記作業と並行して[spet_words.txt](https://github.com/aitokyolab/make_pn_dic/blob/master/definepn/dic/spet_words.txt)、[stop_words.txt](https://github.com/aitokyolab/make_pn_dic/blob/master/definepn/dic/stop_words.txt)を手更新。
- [x] ニュースフォルダ02(CSV形式)を基本として、固有名詞(mecab-ipadic-neolod)にしぼり、新語を抽出し、共起関係のみで極性更新するプログラムを作った。
- [x] [make_pn.py](https://github.com/aitokyolab/make_pn_dic/blob/feature_updpn/definepn/src/make_pn.py)で、森友、マデュラがPositiveなところなど、例外を手修正。
- [x] [update_propn.py](https://github.com/aitokyolab/make_pn_dic/blob/feature_updpn/definepn/src/update_propn.py)にsrcの３プログラムをconcatしてフォルダを引数に一度に設定できるようにした
- [x] make_pn.pyの出力CSVを自動に極性辞書に置き換える仕様

- [ ] 極性更新アルゴリズムの改善(ML,etc)