from django.http import JsonResponse
from account.api.get_user import get_user
from account.models import Vendor


def get_vendor(func):
    """ Utility decorator to get the vendor(service provider) of a request."""
    @get_user
    def inner(request, user, *args, **kwargs):

        vendor = Vendor.objects.filter(user=user).first()
        if not vendor:
            return JsonResponse({"message": "User not registered as a vendor."}, status=401)

        if vendor.approval_status == "pending":
            return JsonResponse({"message": "Vendor not approved yet."}, status=401)

        if vendor.approval_status == "rejected":
            return JsonResponse({"message": "Vendor rejected."}, status=401)

        return func(request, vendor, *args, **kwargs)

    return inner
