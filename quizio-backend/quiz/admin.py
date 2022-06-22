from django.contrib import admin
from .models import Question , Challange

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('course', 'question', 'correct_option',)

class ChallageAdmin(admin.ModelAdmin):
    list_display = ('challangee' , 'challanger' , 'challangee_score', 'challanger_score',)

admin.site.register(Question, QuestionAdmin)
admin.site.register(Challange, ChallageAdmin)