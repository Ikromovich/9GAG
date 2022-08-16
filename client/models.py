from django.contrib.auth.models import AbstractUser
from django.db import models
from gag.helpers import UploadTo
from django.templatetags.static import static

class User(AbstractUser):
    photo = models.ImageField(upload_to=UploadTo('profile'))

    @property
    def avatar(self):
        if self.photo:
            return self.photo.url
        return static("img/avatar.jpg")

