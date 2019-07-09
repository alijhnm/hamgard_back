import json
import threading
from account.models import Group, User
from account.api import get_user, send_invitation
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods


@csrf_exempt
@get_user.get_user
@require_http_methods(["POST"])
def create_group(request, creator):
    data = json.loads(request.body)

    name = data.get("name")
    emails = [i for i in data.get("emails") if i]
    group_type = data.get('type', 'private')
    summary = data.get('summary')
    members = User.objects.filter(email__in=emails)
    unregistered_members = emails
    for user in members:
        unregistered_members.remove(user.email)

    invitation_thread = threading.Thread(target=send_invitation.send_invitation_to_nonusers,
                                         args=[creator.username,
                                               name,
                                               [member.username for member in members],
                                               unregistered_members])
    invitation_thread.start()
    # send_invitation.send_invitation_to_nonusers(creator.username,
    #                                             name,
    #                                             [member.username for member in members],
    #                                             unregistered_members)

    group_id = create_group_in_db(creator, name, group_type, members, summary)

    return JsonResponse({"status": "Successfully created group.",
                         "group id": group_id,
                         "name": name,
                         "type": group_type,
                         "summary": summary,
                         "Added members": [member.username for member in members],
                         "Invited to Hamgard": unregistered_members})


def create_group_in_db(creator, name, type, members, summary):
    group = Group(creator=creator, name=name, type=type, summary=summary)
    group.save()
    for user in members:
        print(user.email)
        group.members.add(user)
        group.save()
    return group.pk
