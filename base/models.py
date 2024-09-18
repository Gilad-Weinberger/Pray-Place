from django.db import models

class Pray(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    address = models.TextField()
    phone = models.CharField(max_length=10)
    email = models.EmailField(max_length=200)
    description = models.TextField()
    image = models.ImageField()

    def __str__(self):
        return f"{self.name}"

class Event(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    date = models.DateTimeField()
    description = models.TextField()
    pray = models.ForeignKey(Pray, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} | {self.date}"

class Photo(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField()
    caption = models.CharField(max_length=200)
    description = models.TextField()
    Pray = models.ForeignKey(Pray, on_delete=models.CASCADE)