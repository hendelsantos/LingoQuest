from django.contrib import admin

from .models import Choice, Course, Lesson, Question, Unit


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 0


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("prompt", "lesson", "position", "weight")
    list_filter = ("lesson__unit__course", "lesson")
    inlines = (ChoiceInline,)


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ("title", "unit", "skill", "position", "status")
    list_filter = ("status", "skill", "unit__course")
    search_fields = ("title", "summary")


admin.site.register(Course)
admin.site.register(Unit)
