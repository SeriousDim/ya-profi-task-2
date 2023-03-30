from django.db import models


class Participant(models.Model):
    name = models.TextField()
    wish = models.TextField()
    recipient = models.ForeignKey('self', on_delete=models.CASCADE, null=True)


class Group(models.Model):
    name = models.TextField()
    description = models.TextField()
    participants = models.ManyToManyField(Participant, related_name='groups')

