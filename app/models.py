from django.db import models

# Create your models here.



class Article(models.Model):
    #user = models.Fo
    title = models.CharField(max_length=120)
    content = models.TextField()
    active = models.BooleanField(default=True)

    # class Comment():
    #     article = models.Foregnkey(Article)
    #     user = mod,
    #     commnt =
    #     date = 

