# Django
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
# DRF
from rest_framework.routers import DefaultRouter
# Local
from projects.views import (
    CategoriesView,
    ProjectsView
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('auths.urls'))
] + static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
) + static(
    settings.STATIC_URL,
    document_root=settings.STATIC_ROOT
)


router: DefaultRouter = DefaultRouter(
    trailing_slash=True
)
router.register('categories', CategoriesView)
router.register('projects', ProjectsView)

urlpatterns += [
    path('api/v1/', include(router.urls)),
]
