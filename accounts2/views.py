from django.shortcuts import render
from django.views.generic import CreateView, TemplateView
from .forms import Custom2UserCreationForm
from django.urls import reverse_lazy

class SignUp2View(CreateView):
    '''サインアップページのビュー
    
    '''
    # forms.pyで定義したフォームのクラス
    form_class = Custom2UserCreationForm
    # レンダリングするテンプレート
    template_name = "signup3.html"
    # サインアップ完了後のリダイレクト先のURLパターン
    success_url = reverse_lazy('accounts2:signup_success3')

    def form_valid(self, form):
        '''CreateViewクラスのform_valid()をオーバーライド
        
        フォームのバリデーションを通過したときに呼ばれる
        フォームデータの登録を行う
        
        parameters:
          form(django.forms.Form):
            form_classに格納されているCustomUserCreationFormオブジェクト
        Return:
          HttpResponseRedirectオブジェクト:
            スーパークラスのform_valid()の戻り値を返すことで、
            success_urlで設定されているURLにリダイレクトさせる
        '''
        # formオブジェクトのフィールドの値をデータベースに保存
        user = form.save()
        self.object = user
        # 戻り値はスーパークラスのform_valid()の戻り値(HttpResponseRedirect)
        return super().form_valid(form)

class SignUpSuccess2View(TemplateView):
    '''サインアップ成功ページのビュー
    
    '''
    # レンダリングするテンプレート
    template_name = "signup_success3.html"