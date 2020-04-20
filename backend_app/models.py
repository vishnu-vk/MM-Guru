import uuid
from django.db import models

def scramble_filename(instance, filename):
    extension = filename.split(".")[-1]
    return "{}.{}".format(uuid.uuid4(),extension)

# Create your models here.
class UploadImage(models.Model):
    image = models.ImageField(upload_to =scramble_filename)

    