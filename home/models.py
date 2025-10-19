from django.db import models 

# Create your models here.

class Contact (models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    content = models.TextField(max_length=1000)
    phone = models.CharField(max_length=15)
    time = models.DateTimeField(auto_now=True ,blank=True)

    def __str__(self):
        return 'Message From User'+ '--' + self.name + self.email
# Create your models here.

