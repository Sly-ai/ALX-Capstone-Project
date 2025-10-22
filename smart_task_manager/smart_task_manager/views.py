from django.http import HttpResponse

def welcome_view(request):
    return HttpResponse("Welcome to the Smart Task Manager API. Visit /swagger/ for API documentation.")

def api_root_view(request):
    return HttpResponse("API Root. Available endpoints: /api/users/, /api/tasks/, /api/categories/, /api/analytics/. Use /swagger/ for documentation.")