from django.urls import path

from .views import (
    DemoAnswerView,
    DemoAssessmentAnswerView,
    DemoAssessmentDetailView,
    DemoCourseOutlineView,
    DemoCoursesListView,
    DemoLessonDetailView,
)

urlpatterns = [
    path("courses/", DemoCoursesListView.as_view(), name="demo-courses"),
    path(
        "courses/<slug:slug>/outline/", DemoCourseOutlineView.as_view(), name="demo-course-outline"
    ),
    path("lessons/<slug:slug>/", DemoLessonDetailView.as_view(), name="demo-lesson-detail"),
    path("lessons/<slug:slug>/answer/", DemoAnswerView.as_view(), name="demo-answer"),
    path(
        "assessments/a1/<str:moment>/",
        DemoAssessmentDetailView.as_view(),
        name="demo-assessment-detail",
    ),
    path(
        "assessments/a1/<str:moment>/answer/",
        DemoAssessmentAnswerView.as_view(),
        name="demo-assessment-answer",
    ),
]
