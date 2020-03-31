from django.urls import path
from .views import RegistrationEndpoint

urlpatterns = [
    path('register/', view=RegistrationEndpoint.as_view()),
]