
from django.http import HttpResponse,JsonResponse

def home_page(request):
    print("Home page request")
    friend=[
        'sundram',
        'ritik',
        'shubham'
    ]
    return JsonResponse(friend , safe=False)
  #HttpResponse("<h1>This is home page</h1>")