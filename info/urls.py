
# task 1
from django.urls import path
from . import views

# task 2
from .views import PersonListCreateView, PersonDetailView


urlpatterns = [ 
    # task 1
    path('', views.api_get_example_slack_info, name='api_get_example_slack_info'),

    # task 2
    path('persons/', PersonListCreateView.as_view()),
    path('persons/<int:pk>/', PersonDetailView.as_view()),
]
