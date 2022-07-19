from django.db import models
from django.urls import reverse
# Create your models here.


class Link(models.Model):
    link_name = models.CharField(max_length=200, null=True)
    link_text = models.CharField(max_length=200)
    link_status_code = models.BooleanField(default=False, blank=True, null=True)

    class Meta:  
        db_table = "link"

    def __str__(self):
        return self.link_text

    def get_absolute_url(self):
        return reverse('index')

            
 