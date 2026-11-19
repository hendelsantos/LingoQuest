from django.contrib import admin

from .models import (
    AttemptAnswer,
    Choice,
    Course,
    Enrollment,
    Lesson,
    LessonAttempt,
    LessonProgress,
    Question,
    Unit,
)


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


class AttemptAnswerInline(admin.TabularInline):
    model = AttemptAnswer
    extra = 0
    can_delete = False
    readonly_fields = (
        "question",
        "selected_choice",
        "response_data",
        "feedback",
        "is_correct",
        "answered_at",
    )


@admin.register(LessonAttempt)
class LessonAttemptAdmin(admin.ModelAdmin):
    list_display = (
        "student",
        "lesson",
        "status",
        "score_percent",
        "passed",
        "xp_awarded",
        "started_at",
    )
    list_filter = ("status", "passed", "lesson__unit__course")
    search_fields = ("student__email", "student__name", "lesson__title")
    readonly_fields = (
        "student",
        "lesson",
        "status",
        "started_at",
        "submitted_at",
        "correct_count",
        "total_questions",
        "score_percent",
        "passed",
        "xp_awarded",
    )
    inlines = (AttemptAnswerInline,)

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(LessonProgress)
class LessonProgressAdmin(admin.ModelAdmin):
    list_display = (
        "student",
        "lesson",
        "best_score",
        "completed",
        "last_attempt_at",
    )
    list_filter = ("completed", "lesson__unit__course")
    search_fields = ("student__email", "student__name", "lesson__title")
    readonly_fields = (
        "student",
        "lesson",
        "best_score",
        "completed",
        "first_passed_at",
        "last_attempt_at",
    )

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
