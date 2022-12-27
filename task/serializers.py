from rest_framework import serializers
from . import models
from accounts.serializers import RegisterSerializer

class TaskSerializer(serializers.ModelSerializer):
    # hourly_rate = serializers.IntegerField(source="assignee.hourly_rate")

    class Meta:
        model = models.Task
        fields = (
            'id','title','description', 'status', 'assignee', 'comment', 'working_hours',
        )
        # update fields


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TaskRating
        fields = (
            'id', 'task', 'user', 'description', 'rate',
        )


class UpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Task
        fields = (
            'id', 'status', 'comment', 'working_hours',
        )


class SalarySerializer(serializers.ModelSerializer):
    # hourly_rate = serializers.SerializerMethodField()

    # hourly_rate = serializers.IntegerField(source="assignee.hourly_rate")

    class Meta:
        model = models.Task
        fields = (
            'working_hours', 'hourly_rate', 'id'
        )

    # def get_hourly_rate(self, obj):
    #     return obj.assignee.hourly_rate