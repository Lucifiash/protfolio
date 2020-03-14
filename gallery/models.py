from django.db import models

# Create your models here.
class Gallery(models.Model):
    descripiton = models.CharField(default="在这写作品的描述",max_length=100)
    #增加图片功能
    image = models.ImageField(default="defalut.png" , upload_to ="images/")
    title = models.CharField(default="作品标题",max_length=50)

    def __str__(self):
       return  self.title
