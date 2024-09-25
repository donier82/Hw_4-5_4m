from django.db import models

# Create your models here.
class Settings(models.Model):
    logo = models.ImageField(upload_to="logo_image/")
    title = models.CharField(max_length=155, verbose_name="Заголовок")
    water_mark = models.CharField(max_length=155, verbose_name="Водяной знак на баннере")
  

    def __str__(self) -> str:
        return "настройки GEEKS"
    

    
    class Meta:
        verbose_name = ""
        verbose_name_plural = "Основные настройки GEEKS"

class News(models.Model):
    title = models.CharField(max_length=155, verbose_name="новости дня")
    image1 = models.ImageField(upload_to="logo_image/", verbose_name='фото_1')
    image2 = models.ImageField(upload_to="logo_image/", verbose_name='фото_2')
    image3 = models.ImageField(upload_to="logo_image/", verbose_name='фото_3')
    text1 = models.CharField(max_length=155, verbose_name="первое новости")  
    text2 = models.CharField(max_length=155, verbose_name="второе новости")  
    text3 = models.CharField(max_length=155, verbose_name="третое новости")  
  

    def __str__(self) -> str:
        return "Новости дня"
    
    class Meta:
        verbose_name = ""
        verbose_name_plural = " настройки Новости"