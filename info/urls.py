from django.urls import path
from . import views

urlpatterns = [
    path('api/', views.api_get_example_slack_info, name='api_get_example_slack_info'),
]
