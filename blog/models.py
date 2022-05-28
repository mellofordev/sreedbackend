from django.db import models

# Create your models here.
tags=(('tech','#tech'),('engineering','#engineering'),('review','review'))
class Blog(models.Model):
    title=models.CharField(max_length=20)
    tag=models.CharField(choices=tags,default='tech',max_length=15)
    content=models.TextField() 
    def __str__(self):
        return self.title
    
