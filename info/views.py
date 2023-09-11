# task 1

from django.http import JsonResponse
import datetime
from django.utils import timezone

# task 2

from rest_framework import generics
from .models import Person
from .serializers import PersonSerializer
from rest_framework.response import Response
from rest_framework.permissions import AllowAny


# task 1

def api_get_example_slack_info(request):
    # Get query parameters
    slack_name = request.GET.get('slack_name', 'example_name')
    track = request.GET.get('track', 'backend')
    
    # Get current day of the week
    current_day = datetime.datetime.now().strftime('%A')
    
    # Get current UTC time with timezone validation
    utc_time = timezone.now()
    if utc_time.tzinfo is None or utc_time.tzinfo.utcoffset(utc_time) != datetime.timedelta(minutes=0):
        return JsonResponse({"error": "Invalid UTC time"}, status=400)
    
    # Define GitHub URLs
    github_file_url = "https://github.com/Pascal-Owilly/zuri.git"
    github_repo_url = "https://github.com/Pascal-Owilly/zuri"
    
    # Prepare the JSON response
    response_data = {
        "slack_name": slack_name,
        "current_day": current_day,
        "utc_time": utc_time.strftime('%Y-%m-%dT%H:%M:%SZ'),
        "track": track,
        "github_file_url": github_file_url,
        "github_repo_url": github_repo_url,
        "status_code": 200
    }
    
    return JsonResponse(response_data)

# task 2


class PersonListCreateView(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    permission_classes = (AllowAny,)


class PersonDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    permission_classes = (AllowAny,)

