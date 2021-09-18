from django.contrib import admin

# Register your models here.
from myDemoApp1.models import Test, Contact, Tag

# 自定义修改Tag内联显示
class TagInline(admin.TabularInline):
    model = Tag

# 自定义admin的contact页面
class ContactAdmin(admin.ModelAdmin):
    # 自定义显示元素
    # fields = ('name', 'age', 'email')

    # 增加list_display属性,在界面展示,默认只展示contact对象
    list_display = ('name', 'age', 'email')  # list
    # 增加搜索功能
    search_fields = ('name',)
    # 自定义内联字段
    inlines = [TagInline]  # Inline
    # 自定义页面分组显示
    fieldsets = (
        ['Main',{
            'fields':('name','age'),
        }],
        ['Advance',{
            'classes': ('collapse',), # CSS
            'fields': ('email',),
        }]
    )

admin.site.register(Contact, ContactAdmin)
admin.site.register([Test, Tag])

