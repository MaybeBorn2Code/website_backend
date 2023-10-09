# Django
from django.urls import path

# Local
from .views import (
    Authorization, Registration, Logout
)


urlpatterns = [
    path('login/', Authorization.as_view()),
    path('reg/', Registration.as_view()),
    path('logout/', Logout.as_view()),
]

