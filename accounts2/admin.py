from django.contrib import admin
# Custom2Userをインポート
from .models import Custom2User

class Custom2UserAdmin(admin.ModelAdmin):
  '''管理ページのレコード一覧に表示するカラムを設定するクラス
  
  '''
  # レコード一覧にidとusernameを表示
  list_display = ('id', 'username')
  # 表示するカラムにリンクを設定
  list_display_links = ('id', 'username')

# Django管理サイトにCustom2User、Custom2UserAdminを登録する
admin.site.register(Custom2User, Custom2UserAdmin)
