from django.db import models

# Create your models here.
class Priority(models.Model):
    name = models.CharField(max_length=50)
    '''
    name has three options:
        baja
        media
        alta
    '''

    def __str__(self):
        return self.name
        
class Task(models.Model):
    title = models.CharField(max_length=100, null=False)
    description = models.TextField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)
    priority = models.ForeignKey(Priority, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.title} - {self.description}"