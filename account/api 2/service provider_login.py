import json
from django.http import JsonResponse

def log_in(request):

    data = json.loads(request.body)
    username = data.get('username')
    password = data.get('password')

    if username is None or password is None:
        return JsonResponse({"message": "invalid params give"}, status=400)







