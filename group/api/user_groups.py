from django.views.decorators.http import require_http_methods
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from account.models import *
from account.api.get_user import get_user
from django.db.models import Q

@csrf_exempt
@get_user
@require_http_methods(['GET'])
def user_groups(request):
    groups = Group.objects.filter(user=request.user).distinct()
    g = []
    index = 0
    for i in groups:
        group_members_count = i.member.all().count()
        g.append(dict(name=i.group.name, admin=i.group.admin.username, id=i.group.id,
                      admin_id=i.group.admin.id, admin_email=i.group.admin.email,
                      members_count=group_members_count,index=index))
        index += 1
    print(g)
    return JsonResponse(g, safe=False, status=200)
