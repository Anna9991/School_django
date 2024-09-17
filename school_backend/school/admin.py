from django.contrib import admin
from .models import Teacher, Lesson, Faq, SchoolInfo, Review

# Register your models here.
admin.site.register(Teacher)
admin.site.register(Lesson)
admin.site.register(Faq)
admin.site.register(Review)

@admin.register(SchoolInfo)
class SchoolInfoAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if SchoolInfo.objects.exists():
            return False
        return super().has_add_permission(request)

    def has_delete_permission(self, request, obj=None):
        return False