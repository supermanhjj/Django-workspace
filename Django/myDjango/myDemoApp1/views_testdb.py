# -*- coding: utf-8 -*-

from django.http import HttpResponse

from myDemoApp1.models import Test

#数据库操作
def testdb(request):
    # test1 = Test(name = "hjj")
    # test1.save()
    # return HttpResponse("<p>数据库添加成功!</p>")

    #----------------------查询操作---------------------#
    #初始化
    response = ''

    # 通过objects这个模型管理器的all()获得所有数据行，相当于SQL中的SELECT * FROM
    list = Test.objects.all()
    for var in list:
        response += var.name + " "

    # filter相当于SQL中的WHERE，可设置条件过滤结果
    response2 = Test.objects.filter(id=1)
    print(response2.get().name)

    # 获取单个对象
    response3 = Test.objects.get(id=1)

    # # 限制返回的数据 相当于 SQL 中的 OFFSET 0 LIMIT 2
    # Test.objects.order_by('name')[0:2]
    # # 数据排序
    # Test.objects.order_by("id")
    # # 上面的方法可以连锁使用
    # Test.objects.filter(name="hjj").order_by("id")

    #-----------------------更新数据-----------------------#
    # 修改其中一个id=2的name字段，再save，相当于SQL中的UPDATE
    test1 = Test.objects.get(id=2)
    test1.name = 'sjj'
    test1.save()

    # 另外一种方式
    # Test.objects.filter(id=1).update(name='sjj')
    # 修改所有的列
    # Test.objects.all().update(name='sjj')

    # -----------------------删除数据-----------------------#
    # 删除id=1的数据
    # test1 = Test.objects.get(id=1)
    # test1.delete()
    # 另外一种方式
    # Test.objects.filter(id=1).delete()
    # 删除所有数据
    # Test.objects.all().delete()

    return HttpResponse("<p>" + response + "</p>")
