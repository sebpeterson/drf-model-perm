from django.db import models

# Create your models here.
class Tool(models.Model):
    """ Tool model """

    id = models.AutoField(primary_key=True)

    # Name
    name = models.CharField(max_length=256, blank=False, null=False)
