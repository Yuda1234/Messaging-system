from django.db import models
from django.contrib.auth.models import User


class ChetMessage(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_chetmessages')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_chetmessages')
    subject = models.CharField(max_length=255)
    message = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.subject} - {self.sender} to {self.receiver}'
