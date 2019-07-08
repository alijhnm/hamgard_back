from django.db import models
from django.contrib.postgres.fields import JSONField


class Poll(models.Model):
    question = models.CharField(max_length=255)
    vote_count = models.IntegerField(default=0)

    def __str__(self):
        return self.question
    
    def is_voted_user(self, user):
        if any(a.is_voted_user(user) for a in self.choices.all()):
            return True
        return False


class PollChoice(models.Model):
    # dictionary = dict(type=None, id=None)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name="choices")
    choice = JSONField(default=dict)
    members = models.ManyToManyField('account.User', blank=True)

    def __str__(self):
        return self.poll.question

    def is_voted_user(self, user):
        try:
            self.members.get(id=user.id)
            return True
        except:
            return False
    

        
# class PollTextChoice(models.Model):
#     poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name="text_choices")
#     text = models.CharField(max_length=200, blank=True, null=True)
#     choice_count = models.IntegerField(blank=True, default=0, null=True)

#     def __str__(self):
#         return self.text

#     def vote(self):
#         self.choice_count += 1


# class PollEventChoice(models.Model):
#     poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name="event_choices")
#     event = models.ForeignKey('event.Event', on_delete=models.CASCADE)
#     choice_count = models.IntegerField(blank=True, default=0, null=True)

#     def __str__(self):
#         return self.event.name

#     def vote(self):
#         self.choice_count += 1
