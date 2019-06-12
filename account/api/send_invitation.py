import smtplib


def send_invitation_to_nonusers(creator_name, group_name, other_members, emails):
    """Sends invitation message to emails that the group creator provides."""

    username = "hamgard.invitation@gmail.com"
    password = "Tahlil9798"

    retry_attempts = 5

    email_text = """
        You are receiving this email because {creator_name} has invited you to join him 
        in {group_name} group on Hamgard.

        Hamgard is an online tour and travel planner with exclusive offers on selected restaurants, cinemas, cafe's and ....

        Members currently in {group_name}:
        {other_members}

        visit Hamgard.com for more info.

        - Best regards
        - Hamgard development team
        """
    
    for i in range(retry_attempts):
        try:

            server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
            server.ehlo()
            server.login(username, password)
            break
        except Exception as e:
            # print("unable to connect to server\nError text: {error_text}".format(error_text=e))
            return

    email_text = email_text.format(creator_name=creator_name, group_name=group_name, other_members="\n\t".join(other_members))

    accepted_emails = check_mail_address(emails)
    for receiver in accepted_emails:
        try:
            server.sendmail(username, receiver, email_text)
            # print('Email sent to {receiver}'.format(receiver=receiver))
        except Exception as e:
            pass
            # print("ERROR: ", e)
    server.close()


def check_mail_address(emails):
    """
    Takes the emails that the user provides and checks for errors in email address.
    Return the emails that are valid and can receive invitations message.
    """
    approved = []
    for email in emails:
        if email.find("..") != -1:
            continue

        if email.count("@") != 1:
            continue

        space_split = email.split()
        if len(space_split) > 1:
            continue

        at_split = email.split("@")
        if len(at_split) != 2:
            continue

        dot_split = at_split[1].split(".")
        if len(dot_split) != 2:
            continue
        approved.append(email)
    return approved
