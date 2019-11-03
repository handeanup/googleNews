from django.db import models

class News(models.Model):
    title = models.CharField(max_length=500,blank=False)
    link = models.URLField(max_length=200)
    guid = models.TextField()
    publish_date = models.CharField(max_length=50)
    source_title = models.CharField(max_length=50,blank=True)
    source_link = models.URLField(max_length=200)
    description = models.TextField()    

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("News_detail", kwargs={"pk": self.pk})
