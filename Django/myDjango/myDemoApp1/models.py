from django.db import models

# Create your models here.
# after add models, do this cmd, create tables
# $ python manage.py makemigrations myDemoApp1  # 让 Django 知道我们在我们的模型有一些变更
# $ python manage.py migrate myDemoApp1   # 创建表结构

# 类继承了models.Model
# 类名代表了数据库表名
# 类里面的字段代表数据表中的字段(name)
# 数据类型则由CharField（相当于varchar）、DateField（相当于datetime）， max_length 参数限定长度

# class UserInfo(models.Model):
#     username = models.CharField(max_length=32)
#     password = models.CharField(max_length=64)

class Test(models.Model):
    name = models.CharField(max_length=20)

# 学习自定义admin管理页面使用
class Contact(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField(default=0)
    email = models.EmailField()
    def __unicode__(self):
        return self.name

# 学习自定义admin管理页面使用
class Tag(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE,)
    name = models.CharField(max_length=50)
    def __unicode__(self):
        return self.name

class Book(models.Model):
    # id = models.AutoField(primary_key=True)  # id 会自动创建,可以手动写入
    # title = models.CharField(max_length=32)  # 书籍名称
    # price = models.DecimalField(max_digits=5, decimal_places=2)  # 书籍价格
    # publish = models.CharField(max_length=32)  # 出版社名称
    # pub_date = models.DateField()  # 出版时间
    title = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    pub_date = models.DateField()
    publish = models.ForeignKey("Publish", on_delete=models.CASCADE)
    authors = models.ManyToManyField("Author")

class Publish(models.Model):
    name = models.CharField(max_length=32)
    city = models.CharField(max_length=64)
    email = models.EmailField()


class Author(models.Model):
    name = models.CharField(max_length=32)
    age = models.SmallIntegerField()
    au_detail = models.OneToOneField("AuthorDetail", on_delete=models.CASCADE)


class AuthorDetail(models.Model):
    gender_choices = (
        (0, "女"),
        (1, "男"),
        (2, "保密"),
    )
    gender = models.SmallIntegerField(choices=gender_choices)
    tel = models.CharField(max_length=32)
    addr = models.CharField(max_length=64)
    birthday = models.DateField()

class Emp(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    salary = models.DecimalField(max_digits=8, decimal_places=2)
    dep = models.CharField(max_length=32)
    province = models.CharField(max_length=32)

class Emps(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    salary =     models.DecimalField(max_digits=8, decimal_places=2)
    dep = models.ForeignKey("Dep", on_delete=models.CASCADE)
    province = models.CharField(max_length=32)
class Dep(models.Model):
    title = models.CharField(max_length=32)