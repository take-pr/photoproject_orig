from django.contrib import admin
from django.urls import path, include # include追加
# auth.viewsをインポートしてauth_viewという記名で利用する
from django.contrib.auth import views as auth_views
# settingsを追加
from django.conf import settings
# staticを追加
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    
    # photo.urlsへのURLパターン
    path('', include('photo2.urls')),

    # accounts2.urlsへのURLパターン
    path('', include('accounts2.urls')),

    # パスワードリセットのためのURLパターン
    # PasswordResetConfirmViewがプロジェクトのurls.pyを参照するのでここに記載
    # パスワードリセット申し込みページ
    path('password_reset/',
         auth_views.PasswordResetView.as_view(
           template_name = "password_reset3.html"),
         name ='password_reset3'),
    
    # メール送信完了ページ
    path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(
           template_name = "password_reset_sent3.html"),
         name ='password_reset_done3'),
    
    # パスワードリセットページ
    path('reset/<uidb64>/<token>',
         auth_views.PasswordResetConfirmView.as_view(
           template_name = "password_reset_form3.html"),
         name ='password_reset_confirm3'),
    
    # パスワードリセット完了ページ
    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(
           template_name = "password_reset_done3.html"),
         name ='password_reset_complete3'),
]

# urlpatternsにmediaフォルダーのURLパターンを追加
urlpatterns += static(
   # MEDIA_URL = '/media/'
  settings.MEDIA_URL,
  # MEDIA_ROOTにリダイレクト
  document_root=settings.MEDIA_ROOT
  )