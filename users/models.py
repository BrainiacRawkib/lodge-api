from django.db import models


class Profile(models.Model):
    user = models.OneToOneField('auth.User', related_name='users', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
