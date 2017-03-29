from django.db import models

# Create your models here.

class UserInfo(models.Model):
    user = models.CharField(max_length=32)
    pwd = models.CharField(max_length=64)
    def __str__(self):
        return self.user
    class Meta:
        verbose_name = "UserInfo"
        verbose_name_plural = "UserInfo"


class Colors(models.Model):
    colors = models.CharField(u'颜色', max_length=10)
    def __str__(self):
        return self.colors
    class Meta:
        verbose_name = "Colors"
        verbose_name_plural = "Colors"



class Ball(models.Model):
    color = models.OneToOneField("Colors")
    description = models.CharField(u'描述', max_length=10)
    def __str__(self):
        return self.description
    class Meta:
        verbose_name = "Ball"
        verbose_name_plural = "Ball"


class Clothes(models.Model):
    color = models.ForeignKey("Colors")
    description = models.CharField(u'描述', max_length=10)
    def __str__(self):
        return self.description
    class Meta:
        verbose_name = "Clothes"
        verbose_name_plural = "Clothes"


class Child(models.Model):
    name = models.CharField(u'姓名', max_length=10)
    sex_choice = ((1, "男"), (0, "女"))
    sex = models.IntegerField(choices=sex_choice, default=0)
    favor = models.ManyToManyField('Colors')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Child"
        verbose_name_plural = "Child"

