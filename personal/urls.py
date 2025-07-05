from django.urls import path
from .views import PersonalView

urlpatterns = [
    path('', PersonalView.as_view(), name='personal_home'),
]
