from django.urls import path
# viewsモジュールをインポート
from . import views
# viewsをインポートしてauth_viewという記名で利用する
from django.contrib.auth import views as auth_views

# URLパターンを逆引きできるように名前を付ける
app_name = 'accounts2'

# URLパターンを登録するための変数
urlpatterns = [
    # サインアップページのビューの呼び出し
    # 「http(s)://<ホスト名>/signup/」へのアクセスに対して、
    # viewsモジュールのSignUpViewをインスタンス化する
    path('signup3/',
         views.SignUp2View.as_view(),
         name='signup3'),
    
    # サインアップ完了ページのビューの呼び出し
    # 「http(s)://<ホスト名>/signup_success/」へのアクセスに対して、
    # viewsモジュールのSignUpSuccessViewをインスタンス化する
    path('signup_success3/',
         views.SignUpSuccess2View.as_view(),
         name='signup_success3'),
    
    # ログインページの表示
    # 「http(s)://<ホスト名>/signup/」へのアクセスに対して、
    # django.contrib.auth.views.LoginViewをインスタンス化して
    # ログインページを表示する
    path('login3/',
         # ログイン用のテンプレート(フォーム)をレンダリング
         auth_views.LoginView.as_view(template_name='login3.html'),
         name='login3'
         ),
    
    # ログアウトを実行
    # 「http(s)://<ホスト名>/logout/」へのアクセスに対して、
    # django.contrib.auth.views.logoutViewをインスタンス化して
    # ログアウトさせる
    path('logout3/',
         auth_views.LogoutView.as_view(template_name='logout3.html'),
         name='logout3'
         ),
]