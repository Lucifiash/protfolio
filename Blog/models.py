from django.db import models

# Create your models here.
class Blog(models.Model):
    # mc tab键
    title = models.CharField(default="文章标题", max_length=50)
    # md
    date = models.DateField()
    #mi
    image =models.ImageField(default="default.png", upload_to="images/")
    #mt
    text = models.TextField(default="文章正文")
    def __str__(self):
        return self.title
