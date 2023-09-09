from django.http import JsonResponse
from datetime import datetime
import pytz

def get_info(request):
    slack_name = request.GET.get('slack_name')
    track = request.GET.get('track')

    # Get the current day of the week
    current_day = datetime.now(pytz.utc).strftime('%A')

    # Get the current UTC time within a +/-2 minute window
    utc_time = datetime.now(pytz.utc).strftime('%Y-%m-%dT%H:%M:%SZ')

    # GitHub file and repository URLs
    github_file_url = "https://github.com/username/repo/blob/main/file_name.ext"
    github_repo_url = "https://github.com/username/repo"

    # Create the JSON response
    response_data = {
        "slack_name": 'pascal_owilly',
        "current_day": current_day,
        "utc_time": utc_time,
        "track": 'backend',
        "github_file_url": github_file_url,
        "github_repo_url": github_repo_url,
        "status_code": 200
    }

    return JsonResponse(response_data)
