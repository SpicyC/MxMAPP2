from django.db import models

# Create your models here.

class Profile (models.Model):
    name= models.CharField(max_length=225)
    citystate= models.CharField(max_length=225)
    email= models.EmailField(max_length=225)

    def __str__(self):
      return f"{self.name} from {self.citystate}"


class Bio (models.Model):
    interests= models.CharField(max_length=225)
    about= models.CharField(max_length=225)
    def __str__(self):
        
      return f"{self.interests} from {self.about}" 