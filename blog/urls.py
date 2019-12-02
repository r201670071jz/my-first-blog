from django.urls import path
from . import views

urlpatterns =[
    path('',views.post_list,name='post_list'),
    path('post/<int:pk>/',views.post_detail,name='post_detail')
    #投稿の詳細ページ用のurl設定
    #投稿ページが増えるごとに毎回urlを設定するのはめんどくさい。
    #そういう場合に設定するのが<>
    #中身はデータ型:変数となっていおり、上記例ではpost/5とした場合はpkという変数にint(5)を代入し、view関数に渡す
]