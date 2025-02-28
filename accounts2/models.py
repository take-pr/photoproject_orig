from django.db import models
# AbstractUserクラスをインポート
from django.contrib.auth.models import AbstractUser

class Custom2User(AbstractUser):
    '''
    Userモデルを継承したカスタムユーザーモデル
    '''
    pass
