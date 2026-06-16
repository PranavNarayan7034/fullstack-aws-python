from django.http import JsonResponse

def home(request):
    return JsonResponse(
        {
            "message": "HELLO WELCOME TO DJANGO BACKEND SERVER"
        }
    )    