from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect, reverse
from myDemoApp1 import models
from myDemoApp1.My_Forms import EmpForm
from django.core.exceptions import ValidationError

# 当采用客户端象 django 的服务器提交 post 请求时，会得到403，权限异常。
# 因为 django 针对提交的请求，有校验。
# 引入csrf_exempt模块,方法前面加入装饰器,解决这个问题
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib import auth

def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    username = request.POST.get("username")
    password = request.POST.get("pwd")
    if username and password:
        # user_obj = models.UserInfo.objects.filter(username=username, password=password).first()
        # print(user_obj.username)
        user_obj = auth.authenticate(username=username, password=password)
        if not user_obj:
            return redirect("/login/")
        else:
            print(user_obj.username)
            rep = redirect("/index/")
            rep.set_cookie("is_login", True)
            return rep

    register_usename = request.POST.get("register_username")
    register_password = request.POST.get("register_pwd")
    context={}
    try:
        User.objects.create_user(username=register_usename, password=register_password)
    except:
        context['Register_resoult'] = "Register Failed"
        return render(request, "login.html", context)
    else:
        # return redirect("/login/")
        context['Register_resoult'] = "Register Success"
        return render(request, "login.html", context)

def index(request):
    print(request.COOKIES.get('is_login'))
    # 收到浏览器的再次请求,判断浏览器携带的cookie是不是登录成功的时候响应的 cookie
    status = request.COOKIES.get('is_login')
    if not status:
        return redirect('/login/')
    return render(request, "index.html")


def logout(request):
    # 点击注销后执行,删除cookie,不再保存用户状态，并弹到登录页面
    rep = redirect('/login/')
    rep.delete_cookie("is_login")
    return rep


def order(request):
    print(request.COOKIES.get('is_login'))
    status = request.COOKIES.get('is_login')
    if not status:
        return redirect('/login/')
    return render(request, "order.html")

@csrf_exempt
def hello(request):
    return HttpResponse("Hello World!!")

# @csrf_exempt
# def login(request):
#     context = {}
#     # context['views_name'] = "Super's web"
#
#     if request.method == "GET":
#         return render(request, "login.html")
#         # return HttpResponse("登录页面get")
#     else:
#         username = request.POST.get('username')
#         pwd = request.POST.get('pwd')
#         if username == "hjj" and pwd == "hjj":
#             return HttpResponse("登录页面-登录成功")
#         else:
#             # return redirect(reversed('login'))
#             return redirect("login")

def test(request):
    context = {}
    context['views_name'] = "Hjj Django"

    context['views_list'] = ['list_0', 'list_1', 'list_2']
    context['views_dict'] = {"name0":"dict_0", "name1":"dict_1"}

    context['hello'] = "Hello World !!!"

    import datetime
    nowtime = datetime.datetime.now()
    context['now_time'] = nowtime

    context['url_str'] = "<a href='https://www.baidu.com/'>点击跳转baidu</a>"

    context['num'] = 95
    return render(request, 'test.html', context)

def add_book(request):
    # 方法1
    book = models.Book(title="第一本书", price=300, publish="南京出版社", pub_date="2008-8-8")
    book.save()
    # 方法2
    books = models.Book.objects.create(title="第二本书", price=200, publish="上海出版社", pub_date="2010-10-10")

    return HttpResponse("<p>数据添加成功！</p>")

def search_book(request):
    books = models.Book.objects.all()
    for i in books:
        print(i.title)

    books = models.Book.objects.filter(pk=4).get().title
    count = models.Book.objects.count()
    print(count)

    return HttpResponse("<p>查找成功！</p>")

# def add_emp(request):
#     if request.method == "GET":
#         form = EmpForm()
#         return render(request, "add_emp.html", {"form": form})
#     else:
#         form = EmpForm(request.POST)
#         if form.is_valid():  # 进行数据校验
#             # 校验成功
#             data = form.cleaned_data  # 校验成功的值，会放在cleaned_data里。
#             data.pop('r_salary')
#             print(data)
#
#             models.Emp.objects.create(**data)
#             return HttpResponse(
#                 'ok'
#             )
#             # return render(request, "add_emp.html", {"form": form})
#         else:
#             print(form.errors)    # 打印错误信息
#             clean_errors = form.errors.get("__all__")
#             print(222, clean_errors)
#         return render(request, "add_emp.html", {"form": form, "clean_errors": clean_errors})

def add_emp(request):
    if request.method == "GET":
        form = EmpForm()  # 初始化form对象
        return render(request, "add_emp.html", {"form":form})
    else:
        form = EmpForm(request.POST)  # 将数据传给form对象
        if form.is_valid():  # 进行校验
            data = form.cleaned_data
            data.pop("r_salary")
            models.Emp.objects.create(**data)
            return redirect("/index/")
        else:  # 校验失败
            clear_errors = form.errors.get("__all__")  # 获取全局钩子错误信息
            return render(request, "add_emp.html", {"form": form, "clear_errors": clear_errors})