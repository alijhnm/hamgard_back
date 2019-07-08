from django.db import models


class Poll(models.Model):
    question = models.CharField(max_length=255)
    vote_count = models.IntegerField(default=0)

    def __str__(self):
        return self.question


class PollTextChoice(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name="text_choices")
    text = models.CharField(max_length=200, blank=True, null=True)
    choice_count = models.IntegerField(blank=True, default=0, null=True)

    def __str__(self):
        return self.text

    def vote(self):
        self.choice_count += 1


class PollEventChoice(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name="event_choices")
    event = models.ForeignKey('event.Event', on_delete=models.CASCADE)
    choice_count = models.IntegerField(blank=True, default=0, null=True)

    def __str__(self):
        return self.event.name

    def vote(self):
        self.choice_count += 1
