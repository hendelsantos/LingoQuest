from django.contrib import admin

from .models import Choice, Course, Enrollment, Lesson, Question, Unit


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


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ("student", "course", "status", "enrolled_at", "ended_at")
    list_filter = ("status", "course")
    search_fields = ("student__email", "student__name", "course__title")
    autocomplete_fields = ("student",)
