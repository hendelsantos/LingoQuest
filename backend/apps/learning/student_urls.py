from django.urls import path

from .views import (
    AuthorizedAnswerView,
    AuthorizedCourseOutlineView,
    AuthorizedLessonDetailView,
    StudentEnrollmentListView,
)

urlpatterns = [
    path("me/enrollments/", StudentEnrollmentListView.as_view(), name="student-enrollments"),
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
        "lessons/<slug:slug>/answer/",
        AuthorizedAnswerView.as_view(),
        name="authorized-answer",
    ),
]
