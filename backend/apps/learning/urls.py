from django.urls import path

from .views import DemoAnswerView, DemoCourseOutlineView, DemoLessonDetailView

urlpatterns = [
    path(
        "courses/<slug:slug>/outline/", DemoCourseOutlineView.as_view(), name="demo-course-outline"
    ),
    path("lessons/<slug:slug>/", DemoLessonDetailView.as_view(), name="demo-lesson-detail"),
    path("lessons/<slug:slug>/answer/", DemoAnswerView.as_view(), name="demo-answer"),
]
