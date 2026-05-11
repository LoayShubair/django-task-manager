from django.db import models


class OpenTaskManager(models.Manager):
    def open(self):
        return self.filter(status="open")


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=20, default="open")
    objects = OpenTaskManager()

    def __str__(self):
        return f"{self.title} - {self.status}"

    class Meta:
        ordering = ["title"]
