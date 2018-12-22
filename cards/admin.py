from django.contrib import admin
from ordered_model.admin import OrderedTabularInline, OrderedStackedInline, OrderedInlineModelAdminMixin, OrderedModelAdmin

from .models import Owner, Website, Page, Question, Choice, Answer

class WebsiteInline(admin.StackedInline):
    model = Website


class OwnerAdmin(admin.ModelAdmin):
    inlines = [WebsiteInline,]


class PageInline(admin.TabularInline):
    model = Page


class WebsiteAdmin(admin.ModelAdmin):
    inlines = [PageInline,]


class QuestionInline(admin.TabularInline):
    model = Question


class PageAdmin(admin.ModelAdmin):
    inlines = [QuestionInline,]


class ChoiceInline(OrderedTabularInline):
    model = Choice
    extra = 1


class AnswerInline(admin.TabularInline):
    model = Answer


class QuestionAdmin(OrderedModelAdmin):
    list_display = ('question', 'order', 'move_up_down_links')
    inlines = [ChoiceInline, AnswerInline,]


admin.site.register(Owner, OwnerAdmin)
admin.site.register(Website, WebsiteAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(Question, QuestionAdmin)
