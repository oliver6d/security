from django.contrib import admin
from .models import *
##Step 7

# #class UserInline(admin.StackedInline):
# class UserInline(admin.TabularInline):
#     model = User
#     extra = 3


# class QuestionAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None,               {'fields': ['question_text']}),
#         ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
#     ]
#     inlines = [ChoiceInline]
#     list_display = ('question_text', 'pub_date', 'was_published_recently')

admin.site.register(Votable)
admin.site.register(Question)
admin.site.register(Comment)
admin.site.register(Profile)
admin.site.register(Vote)
admin.site.register(Language)
admin.site.register(Country)
admin.site.register(Other)