from django.db import models

class UserName(models.Model):
    session_id = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
