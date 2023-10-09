# Django
from django.contrib import admin

# Local
from .models import Reviews


class ReviewsAdmin(admin.ModelAdmin):
    """Admin Panel for reviews."""

    model = Reviews
    list_display = (
        'user',
        'review',
        'rating',
        'date_created'
    )
    readonly_fields = (
        # 'user',
        # 'review',
        # 'rating',
        'date_created',
    )
    search_fields = (
        'user',
        'rating',
        'date_created'
    )


admin.site.register(Reviews, ReviewsAdmin)

