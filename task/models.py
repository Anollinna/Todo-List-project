from django.db import models


class Task(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    is_done = models.BooleanField(default=False)
    tags = models.ManyToManyField("Tag", related_name="tasks", blank=True)

    def __str__(self):
        return self.content


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
