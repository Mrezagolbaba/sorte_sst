from django.db import models

EVENT_STATUS = (
    ('Done', 'Done'),
    ('Upcoming', 'Upcoming'),
)
# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=200)
    when = models.DateTimeField()
    status = models.CharField(max_length=20, choices=EVENT_STATUS)


    def __str__(self):
        return self.title