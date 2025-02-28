from django.urls import path
from . import views

# URLパターンを逆引きできるように名前を付ける
app_name = 'photo2'

# URLパターンを登録する変数
urlpatterns = [
    # photoアプリへのアクセスはviewsモジュールのIndexViewを実行
    path('', views.Index3View.as_view(), name='index3'),
    
    # 写真投稿ページへのアクセスはviewsモジュールのCreatePhotoViewを実行
    path('post/', views.CreatePhotoView.as_view(), name='post3'),
    
    # 投稿完了ページへのアクセスはviewsモジュールのPostSuccessViewを実行
    path('post_done/',
         views.PostSuccessView.as_view(),
         name='post_done3'),
    
    # カテゴリ一覧ページ
    # photos/<Categorysテーブルのid値>にマッチング
    # <int:category>は辞書{category: id値(int)}としてCategoryViewに渡される
    path('photos/<int:category>',
         views.CategoryView.as_view(),
         name = 'photos_cat3'
         ),

    # ユーザーの投稿一覧ページ
    # photos/<ユーザーテーブルのid値>にマッチング
    # <int:user>は辞書{user: id値(int)}としてCategoryViewに渡される
    path('user-list/<int:user>',
         views.UserView.as_view(),
         name = 'user_list3'
         ),
    
    # 詳細ページ
    # photo-detail/<Photo postsテーブルのid値>にマッチング
    # <int:pk>は辞書{pk: id値(int)}としてDetailViewに渡される
    path('photo-detail/<int:pk>',
         views.DetailView.as_view(),
         name = 'photo_detail3'
         ),
    
    # マイページ
    # mypage/へのアクセスはMypageViewを実行
    path('mypage/', views.MypageView.as_view(), name = 'mypage3'),

    # 投稿写真の削除
    # photo/<Photo postsテーブルのid値>/delete/にマッチング
    # <int:pk>は辞書{pk: id値(int)}としてDetailViewに渡される
    path('photo/<int:pk>/delete/',
         views.PhotoDeleteView.as_view(),
         name = 'photo_delete3'
         ),
     
    # 検索機能
    # search/へのアクセスはSearchViewを実行
    path('search/', views.SearchView.as_view(),
          name='search_results3'
         ),
]
