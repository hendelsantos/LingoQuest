from django.urls import path

from .views import (
    AuthorizedCourseOutlineView,
    AuthorizedLessonDetailView,
    LessonAttemptAnswerView,
    LessonAttemptDetailView,
    LessonAttemptFinishView,
    LessonAttemptStartView,
    StudentEnrollmentListView,
    StudentLearningSummaryView,
)

urlpatterns = [
    path("me/enrollments/", StudentEnrollmentListView.as_view(), name="student-enrollments"),
    path("me/dashboard/", StudentLearningSummaryView.as_view(), name="student-dashboard"),
    path(
        "courses/<slug:slug>/outline/",
        AuthorizedCourseOutlineView.as_view(),
        name="authorized-course-outline",
    ),
    path(
        "lessons/<slug:slug>/",
        AuthorizedLessonDetailView.as_view(),
        name="authorized-lesson-detail",
    ),
    path(
        "lessons/<slug:slug>/attempts/",
        LessonAttemptStartView.as_view(),
        name="lesson-attempt-start",
    ),
    path(
        "attempts/<uuid:attempt_id>/",
        LessonAttemptDetailView.as_view(),
        name="lesson-attempt-detail",
    ),
    path(
        "attempts/<uuid:attempt_id>/answers/",
        LessonAttemptAnswerView.as_view(),
        name="lesson-attempt-answer",
    ),
    path(
        "attempts/<uuid:attempt_id>/finish/",
        LessonAttemptFinishView.as_view(),
        name="lesson-attempt-finish",
    ),
]
