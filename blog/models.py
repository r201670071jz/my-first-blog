#ここではデータベース(モデル)の設定をしているよ。
#データベース(モデル)とはその名の通り、webアプリのデータを集めているところ。
# 例えば、あなたがwebでブログを書くとしよう。
# 「今日の夜ご飯」というタイトルで
# 「今日は夜に友達とラーメンを食べた。おいしかった。」という内容で
# 「2019年11月18日」にブログを書いて投稿した場合、タイトル内容、投稿日のデータはデータベースに保存されるのである。
# 例えば、あなたが為替データから25日分の平均を算出するwebアプリを作った場合、
# 25日分の為替データはデータベースに保存されており、そのデータベースの値を使って平均を算出しブラウザに表示するのである。

# データベースはすべてのデータがごちゃ混ぜになって保存されているわけではない。エクセルにインデックスをつけ保存していくイメージ。
# 上記のブログの例でいうならばエクセルの1行目1列目に「タイトル」、1行2列目に「内容」、1行3列目に「投稿日」といったようにインデックスが
# 作られ、2行目に投稿内容、つまり「今日の夜ご飯」、「今日は夜に友達とラーメンを食べた。おいしかった。」、「2019年11月18日」がくるような感じ。

# このページでは1列目のインデックスに相当する部分を定義する。
# 定義とは、そのインデックスが文字なのか、数字なのか、日付なのかといった
# どのタイプに当てはまるのかを決定し、名前をつけること。
# 例えば、1行目1列目には「タイトル」という名前で、タイプは文字！
# 1行2列目に「内容」という名前でタイプは文字！
# 1行3列目に「投稿日」という名前でタイプは日付！のような感じである。
# 感覚的にはエクセルのインデックスを作って、各インデックスのデータ型を決める作業。

#もともとデータベースの操作（上記でいう定義など）って違う言語で難しいんだけど、それをdjangoがpythonでできるようにした.
#とはいえ、もともとが違う言語であるため、若干pythonらしからぬことがある。
#例えば、変数のtype指定がある。
#pythonは変数を指定するとき、「x=3」でも「x='オザワ'」のように値が数字だろうが、文字だろうが関係なかった。
#しかし、モデルを作る場合はそうではない。上述した通り、そのデータがどのタイプなのか定義してあげなきゃいけない。

#調べた中では基本的には1つのアプリケーションに1つのデータベースにするほうが便利。（アプリごとに機能が分けらるためメンテしやすいからだそう）
#具体的には為替データ用のテーブルとお客様情報テーブルがある場合はkawaseというアプリとokyakuというアプリでmodel.pyを編集すること

from django.db import models
from django.conf import settings
from django.utils import timezone

class Post(models.Model):#データベースの名前。頭文字は大文字。models.ModelはこのクラスはDjangoモデルだよ！って教えるよう
    
    #ForeignKeyは他のモデルへのリンク。つまりモデル同士を紐づけるときに使う。
    #構文はmodels.ForeignKey(参照先のモデル（クラス）名,on_delete.アクション)
    # 第一引数の参照先モデルは基本的には1種類のフィールドのみ
    #on_delete:参照するオブジェクトが削除された(第一引数)ときに、紐づけられたデータをどうするか決めるやつ。
    #on_delet.CASCADEは第一引数がデーターベースから削除された場合にそれを参照しているデータはすべて削除するよという命令。
    # 例えばmodel.pyにArtistというクラス（モデル）とMusicというクラスがあり、それぞれ

    # Artist:ワンオクロック、ウーバーワールド、ラッドウィンプス

    # Music:  title(models.CharField)    artist(models.ForeignKey(Artist,on_delete=model.CASCADE))
    #         キミシダイ列車              ワンオクロック
    #         アンサイズニア              ワンオクロック
    #         SHAMROCK                   ウーバーワールド
    #         金字塔                      ウーバーワールド
    #         オシャカシャマ              ラッドウィンプス
    #         セツナレンサ                ラッドウィンプス

    # とモデルが定義されていたとする。ここでワンオクロックを削除するとそれに付随する「キミシダイ列車」と「アンサイズニア」も削除される

    author =models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)#CharFeildは文字数制限があるフィールド（タイプ）
    text = models.TextField()#TextFeildは文字数がないテキスト用フィールド
    created_date = models.DateTimeField(default = timezone.now)
    published_date = models.DateTimeField(blank=True,null=True)
    #blank＝TRUE:フォームからの投稿時に入力は不要。
    #null=TRUE:データベース値が空でもOK
    #だって下のpubulishメソッドを実行したときにその時の日時が保存されるから

    def publish(self):
        self.published_date = timezone.now()
        self.save()#.save()することでデータベースへ公開される

    def __str__(self):#__str__()を呼ぶとタイトルを出力する
        return self.title

# Create your models here.
