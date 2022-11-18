from django.db import models
from django_quill.fields import QuillField
from django.utils import timezone


class Diary(models.Model):

    title = models.CharField(max_length=100, verbose_name="Title")
    content = QuillField(default ='Write your diary, Today...')
    post_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Diary'
        verbose_name_plural = 'Diaries'


    def __str__(self):
        return self.title
    
   
    
