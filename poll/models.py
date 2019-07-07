from django.db import models


class Poll(models.Model):
    question = models.CharField(max_length=255)

    def __str__(self):
        return self.question


class PollChoice(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name="choices")
    text = models.CharField(max_length=200, blank=True, null=True)
    choice_count = models.IntegerField(blank=True, default=0, null=True)

    def __str__(self):
        return self.text

    def vote(self):
        self.choice_count += 1
