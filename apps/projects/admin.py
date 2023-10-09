# Django
from django.contrib import admin

# Local
from .models import Categories, Projects, Images


class CategoriesAdmin(admin.ModelAdmin):
    """Admin Panel for categories."""

    model = Categories
    list_display = ('title',)
    search_fields = ('title',)


class ProjectsAdmin(admin.ModelAdmin):
    """Admin Panel for projects."""

    model = Projects
    list_display = (
        'title',
        'description',
        'link',
        'category'
    )
    search_fields = (
        'title',
        'category'
    )


admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Projects, ProjectsAdmin)
admin.site.register(Images)

