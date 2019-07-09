from django.db import models


class Comment(models.Model):
    post = models.ForeignKey('event', on_delete=models.CASCADE, related_name='comments')
    writer = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.approved_comment
