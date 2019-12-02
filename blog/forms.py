from django import forms
from .models import Post
class PostForm(forms.ModelForm):#入力フォームの名前をclassで定義。forms.ModelFormはdjangoにこのクラスはモデルフォームだぞと伝える呪文。（モデルフォームはいくつかあるフォームの中の一種で、入力したフォームをモデルに登録できる）
    class Meta:#どのモデルを使うえばいいかを下2行で定義
        model = Post #どのモデルにフォームデータを登録するか定義する
        fields = ('title','text',) #何のフォームを置くのか定義。もちろん1行上で設定したモデルのフィールドを指定すること
        
