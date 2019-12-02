from django.urls import path
from . import views
#Uulpatternsの構文は基本的に以下。
# path('自分が設定したいURL',views.対象となるビュー(オブジェクト),'URLの名前')
#'自分が設定したいURL'では実際にユーザーに叩いてほしいURLを指定する。ここで指定したURLを叩くと処理が実行されるようになる
#views.対象となるビュー(オブジェクト)を定義。どのテンプレートを使って、どのモデルデータを使うなどの詳細はviewで記載するとして、ここではビューの指定のみ
#HTMLのaタグで飛ばしたいページを挿入する場合、djangoでは"{% url 'post_new' %}"のようにURLの名前を指定する。もし、名前の指定がない場合はURLを書く必要があり、めんどくさいしながいよね、

urlpatterns =[
    path('',views.post_list,name='post_list'),
    path('post/<int:pk>/',views.post_detail,name='post_detail'),
    path('post/new/',views.post_new,name="post_new")
    #投稿の詳細ページ用のurl設定
    #投稿ページが増えるごとに毎回urlを設定するのはめんどくさい。
    #そういう場合に設定するのが<>
    #中身はデータ型:変数となっていおり、上記例ではpost/5とした場合はpkという変数にint(5)を代入し、view関数に渡す
]