from django.db import models


# Create your models here.
class Hackathon(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    location = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    organizer = models.ForeignKey(
        "users.User", related_name="hackathons", on_delete=models.CASCADE
    )
    participants = models.ManyToManyField(
        "users.User", related_name="participating_hackathons", default=None, blank=True
    )

    def __str__(self):
        return self.name
