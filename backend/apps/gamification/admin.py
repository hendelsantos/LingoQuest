from django.contrib import admin

from .models import XPEvent


@admin.register(XPEvent)
class XPEventAdmin(admin.ModelAdmin):
    list_display = ("student", "amount", "source_type", "source_id", "created_at")
    list_filter = ("source_type", "created_at")
    search_fields = ("student__email", "student__name", "source_id")
    readonly_fields = (
        "id",
        "student",
        "source_type",
        "source_id",
        "amount",
        "created_at",
    )

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
