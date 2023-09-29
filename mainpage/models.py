from django.db import models

class News(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    pub_date = models.DateTimeField("date published")
    def __str__(self):
        return self.title