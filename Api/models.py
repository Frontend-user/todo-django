from django.db import models

class SpisokModel(models.Model):
    spisok_name = models.CharField(max_length=100)
    def dict(self) -> dict:
        return {
            'spisok_name': self.spisok_name,
            'id': self.id,
        }

class TaskModel(models.Model):
    task_name = models.CharField(max_length=300)
    spisok = models.ForeignKey('SpisokModel', on_delete=models.CASCADE) #ccskсссы сылаемя на список список айди фильтрум по и по какому нибудь списки

    def dict(self) -> dict:
        return {
            'task_name': self.task_name,
            'spisok': self.spisok,
        }