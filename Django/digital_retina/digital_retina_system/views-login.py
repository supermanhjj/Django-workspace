from django.shortcuts import render
from django.shortcuts import redirect
from django.views import View
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.

class Login(View):
    def post(self,request):
        try:
            user = request.POST.get('username',None)
            pwd = request.POST.get('password',None)
            # 验证密码
            obj = auth.authenticate(request,username=user,password=pwd)
            if obj:
                return JsonResponse({'code':'ok','message':'账号密码验证成功'})
        except:
            return JsonResponse({'code':'no','message':'验证失败'})

class Register(View):
    def post(self, request):
        try:
            username = request.POST.get('username',None)
            password = request.POST.get('password',None)
            user = User.objects.create_user(username=username,password=password)
            user.save()
        except:
            return JsonResponse({'code':'no','message':'注册失败'})
        return JsonResponse({'code':'ok','message':'注册成功'})

def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    username = request.POST.get("username")
    password = request.POST.get("pwd")
    valid_num = request.POST.get("valid_num")
    keep_str = request.session.get("keep_str")
    if keep_str.upper() == valid_num.upper():
        user_obj = auth.authenticate(username=username, password=password)
        print(user_obj.username)
        if not user_obj:
            return redirect("/login/")
        else:

            auth.login(request, user_obj)
            path = request.GET.get("next") or "/index/"
            print(path)
            return redirect(path)
    else:
        return redirect("/login/")
