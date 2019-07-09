from django.http import JsonResponse
from account.models import User


def get_user(func):
    """Utility decorator that gets the user of a request using provided token."""

    def inner(request, *args, **kwargs):
        head = request.META
        try:
            token = head.get('HTTP_AUTHORIZATION').split()[1]
            print("messss")
        except AttributeError:
            return JsonResponse({"message": "token not provided in header."}, status=400)

        user = User.objects.filter(token=token)

        if len(user) == 1:
            user = user.first()
        else:
            return JsonResponse({"message": "user not found"}, status=404)

        return func(request, user, *args, ** kwargs)

    return inner
