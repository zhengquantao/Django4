from django import forms
from student import models
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator


class RegForm(forms.Form):
    username = forms.CharField(
        max_length=16,
        label="用户名",
        widget=forms.widgets.TextInput(attrs={"class": "form-control"},),
        error_messages={
            "max_length": "用户名最长16位",
            "required": "用户名不能为空",
        }
    )
    password = forms.CharField(
        min_length=6,
        max_length=10,
        label="密码",
        widget=forms.widgets.PasswordInput(attrs={"class": "form-control"},),
        error_messages={
            "max_length": "最小长度为6",
            "required": "密码不能为空",
        }
    )
    re_password = forms.CharField(
        min_length=6,
        max_length=10,
        label="确认密码",
        widget=forms.widgets.PasswordInput(attrs={"class": "form-control"}, render_value=True),
        error_messages={
            "min_length": "密码最少6位",
            "required": "密码不能为空",
        }
    )
    gender = forms.ChoiceField(
        choices=(('男', "男"), ('女', "女")),
        label="性别",
        initial=1,
        widget=forms.widgets.RadioSelect
    )
    age = forms.CharField(
        max_length=10,
        label="年龄",
        widget=forms.widgets.TextInput(attrs={"class": "form-control"}),

    )
    addr = forms.CharField(
        max_length=32,
        label="地址",
        widget=forms.widgets.TextInput(attrs={"class": "form-control"}),
        error_messages={
            "required": "地址不能为空",
        }
    )
    phone = forms.CharField(
        label="手机",
        validators=[
            RegexValidator(r'^1[3-9][0-9]{9}$', '手机格式不正确')
        ],
        widget=forms.widgets.TextInput(attrs={"class": "form-control"}),
        error_messages={
            "required": "手机不能为空"
        }
    )

    # 重写username字段的局部钩子
    def clean_username(self):
        username = self.cleaned_data.get("username")
        is_exist = models.Student.objects.filter(username=username)
        if is_exist:
            # 表示用户名已注册
            self.add_error("username", ValidationError("用户名已存在！"))
        else:
            return username

        # 重写全局的钩子函数， 对确认密码做效验
    def clean(self):
        password = self.cleaned_data.get("password")
        re_password = self.cleaned_data.get("re_password")
        if re_password and re_password != password:
            self.add_error("re_password", ValidationError("两次密码不一致"))
        else:
            return self.cleaned_data