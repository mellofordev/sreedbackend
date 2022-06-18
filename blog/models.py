from django.db import models

# Create your models here.
tags=(('tech','#tech'),('engineering','#engineering'),('review','#review'))
class Blog(models.Model):
    title=models.CharField(max_length=20)
    tag=models.CharField(choices=tags,default='tech',max_length=15)
    pic=models.ImageField(default='media/postpics/default.jpg',upload_to='postpics',null=False)
    content=models.TextField() 
    def __str__(self):
        return self.title
    
class Project(models.Model):
    project_name=models.CharField(max_length=50)
    pic=models.ImageField(default='media/postpics/default.jpg',upload_to='projectpics')

    def __str__(self):
        return self.project_name
