from django.contrib import admin
# Register your models here.
from .models import Choice, Question
# admin.site.register(Question)
# admin.site.register(Choice)


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'question_text', 'pub_date',)  # 列表显示
    search_fields = ('question_text',)  # 搜索
    list_filter = ('pub_date',)  # 过滤器
    # date_hierarchy = 'birth'            #日期型字段进行层次划分。
    # ordering = ('-birth','age')         #对出生日期降序排列，对年级升序
    # fields = ('name','sex','age','birth','type')    #自定义编辑表单，在编辑表单的时候
    # 显示哪些字段，显示的属性

    # def get_list_display(self, request):
    # return ['id', 'question_text']


class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('question_id', 'choice_text', 'votes',)

    # def get_list_display(self, request):
    # return ['question_id', 'choice_text']
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
