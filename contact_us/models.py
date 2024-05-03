from django.db import models

class ContactUs(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField()
    age = models.IntegerField(default=0)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.name} - {self.email}'


    class Meta:
        verbose_name ='پیام'
        verbose_name_plural = 'پیام ها'