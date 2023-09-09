from django.http import HttpResponse
import json
from datetime import datetime
import pytz

def get_info(request):
    # Get query parameters from the request
    slack_name = request.GET.get('slack_name', '')
    track = request.GET.get('track', '')

    # Get the current day of the week
    current_day = datetime.now(pytz.utc).strftime('%A')

    # Get the current UTC time within a +/-2 minute 
    utc_time = datetime.now(pytz.utc).strftime('%Y-%m-%dT%H:%M:%SZ')

    # GitHub file and repository URLs
    github_file_url = "https://github.com/Pascal-Owilly/zuri-training.git"
    github_repo_url = "https://github.com/Pascal-Owilly/zuri-training"

    # Create the JSON response
    response_data = {
        "slack_name": slack_name,
        "current_day": current_day,
        "utc_time": utc_time,
        "track": track,
        "github_file_url": github_file_url,
        "github_repo_url": github_repo_url,
        "status_code": 200
    }

    # Create an HttpResponse with a custom status message
    response = HttpResponse(json.dumps(response_data), content_type='application/json', status=200)
    response.reason_phrase = 'OK'

    return response
