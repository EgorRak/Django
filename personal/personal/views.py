from django.http import HttpResponse
from datetime import datetime
def hello(request):
    return HttpResponse("OK")
def info(request):
    now = datetime.now()
    return HttpResponse(now)