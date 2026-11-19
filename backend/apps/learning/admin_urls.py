from django.urls import path

from .views import AdminEnrollmentDetailView, AdminEnrollmentListCreateView

urlpatterns = [
    path(
        "enrollments/",
        AdminEnrollmentListCreateView.as_view(),
        name="admin-enrollments",
    ),
    path(
        "enrollments/<uuid:enrollment_id>/",
        AdminEnrollmentDetailView.as_view(),
        name="admin-enrollment-detail",
    ),
]
