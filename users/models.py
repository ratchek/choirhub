from django.contrib.auth import models as auth_models

class User(auth_models.AbstractUser):
    pass
    # add additional fields in here

    def __str__(self):
        return self.username

