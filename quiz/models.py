from distutils.command.upload import upload
from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(verbose_name="Yo'nalishlar nomi", max_length=150)
    reg_date = models.DateField(auto_now_add=True)
    duration = models.DurationField()


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Yo'nalish" 
        verbose_name_plural = "Yo'nalishlar" 

class Question(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name="Yo'nalish")
    text = models.TextField(verbose_name="Savol matni",max_length=250)
    images = models.ManyToManyField('QuestionImage', blank=True, related_name="images")
    answers = models.ManyToManyField('Answer', blank=True, related_name="answers")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Savol" 
        verbose_name_plural = "Savollar" 



class QuestionImage(models.Model):
    image = models.ImageField(upload_to='quiz_image')


class Answer(models.Model):
    text = models.CharField(verbose_name="Javob", max_length=35)
    correct_answer = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Javob" 
        verbose_name_plural = "Javoblar" 

