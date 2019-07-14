from django.db import models

# Create your models here.
class Article(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='序号')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    last_edit_time = models.DateTimeField(auto_now=True, verbose_name='最后一次编辑')
    categories = models.CharField(choices = [
        ('F', 'FilmReview'),
        ('T', 'Tech'),
        ('O','Other')
    ], max_length=20, verbose_name='类别')
    title = models.CharField(max_length=50, verbose_name='标题')
    preview_Img = models.TextField(default='data:image/jpg;base64,', name='预览图片')
    content = models.TextField(default='<p>null<p>', name='正文')
