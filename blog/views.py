from django.shortcuts import render,get_object_or_404,redirect
from .models import Post
from django.utils import timezone
from .forms import PostForm

#view.pyではリクエストがきた（URLを叩いてもらった）時にどのテンプレートにどのモデルのデータを組み合わせて表示するかを決めている。
#基本的には表示するテンプレートやモデルデータが異なれば、viewは新設する必要あり

# Create your views here.
def post_list(request):
    posts=Post.objects.filter(published_date__lte=timezone.now()).order_by("published_date")
    return render(request,'blog/post_list.html',{"postsx":posts})

def post_detail(request,pk):
    post = get_object_or_404(Post,pk=pk)#Postという名のモデルにプライマリーキーがurlのpk変数の値があったらオブジェクトを取りだす(.all()ではなく.get()だから1つのオブジェクトだけ)。なければ404を表示
    return render(request,'blog/post_detail.html',{"postsy":post})
    #テンプレートは基本的には決まったものしか表示しない。しかし、データベースからデータを取り出したりとか、
    #フォームをする場合は｛｝が必要になる。｛｝の構文は以下
    #{'html上での変数名':対象となるモデルやフォームの変数名(このページで指定されている)}

def post_new(request):
    if request.method=="POST":#送信ボタンが押された場合の処理。edit_htmlの<form>タグでPOSTとしたので送信ボタンを押した後はrequestはPOSTとなる。(正確にはrequest.POST)
        form=PostForm(request.POST)#フォームの引数にはrequestを入れるが、送信ボタンを押した後の処理にはrequest.HTMLのフォームメソッド名(今回の場合はPOST)
        if form.is_valid():# .is_valid()ではすべての必須フィールドが設定され、不正な値が送信されないかをチェックしてくれる
            post = form.save(commit=False)#commit=Falseでモデルをまだ保存しないという意味
            post.author = request.user
            post.published_date = timezone.now()
            post.save()#モデルの.save()post_list.htmlではpublish(.save)したものを投稿できるようにしたのでこれが必要
            return redirect('post_detail',pk=post.pk)#作成した投稿へリダイレクトする。構文はredirect('リダイレクトしたいurl名',)

    else:#トップのプラスボタンからedit.htmlに飛ばされた場合
        form = PostForm()
    return render(request,'blog/post_edit.html',{'form':form})
    #テンプレートは基本的には決まったものしか表示しない。しかし、データベースからデータを取り出したりとか、
    #フォームをする場合は｛｝が必要になる。｛｝の構文は以下
    #{'html上での変数名':対象となるモデルやフォームの変数名(このページで指定されている)}