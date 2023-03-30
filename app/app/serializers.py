from rest_framework.fields import IntegerField, CharField
from rest_framework.serializers import ModelSerializer

from .models import Participant, Group


class ParticipantSerializer(ModelSerializer):
    class Meta:
        model = Participant
        fields = ['id', 'name', 'wish']


class GroupSerializer(ModelSerializer):
    participants = ParticipantSerializer()

    class Meta:
        model = Group
        fields = ['id', 'name', 'description', 'participants']
