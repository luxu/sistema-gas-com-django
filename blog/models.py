from django.db import models
from django.utils import timezone



class Usuario(models.Model):
  id =  models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
  name = models.CharField(max_length=200)
  login = models.CharField(max_length=200)
  created_date = models.DateTimeField(default=timezone.now)
  published_date = models.DateTimeField(blank=True, null=True)

  def publish(self):
    self.published_date = timezone.now()
    self.save()

  def __str__(self):
    return self.name

class Post(models.Model):
  author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
  # models.ForeignKey('Usuario',on_delete=models.CASCADE)
  title = models.CharField(max_length=200)
  text = models.TextField()
  created_date = models.DateTimeField(default=timezone.now)
  published_date = models.DateTimeField(blank=True, null=True)

  def publish(self):
    self.published_date = timezone.now()
    self.save()

  def __str__(self):
    return self.title