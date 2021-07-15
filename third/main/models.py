from django.db import models
from django.db.models.deletion import CASCADE


# Create your models here.

class ToDoList(models.Model):
    name = models.CharField(max_length = 200)


    def __str__(self):
        return self.name


class Item(models.Model):
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    text = models.CharField(max_length=350)
    complete = models.BooleanField()


    def __str__(self):
        return self.text