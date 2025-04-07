from django.contrib import admin
from .models import Question, Answer

class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 0

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('title', 'content')
    inlines = [AnswerInline]

class AnswerAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'user', 'created_at', 'total_likes')
    list_filter = ('created_at',)
    search_fields = ('content',)

admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)