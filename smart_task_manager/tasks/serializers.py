from rest_framework import serializers
from .models import Task
from django.utils import timezone

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = ['owner', 'completed_at']

    def validate_due_date(self, value):
        if value < timezone.now():
            raise serializers.ValidationError("Due date must be in the future.")
        return value

    def validate(self, data):
        if data.get('status') == 'Completed' and self.instance and self.instance.status == 'Completed':
            raise serializers.ValidationError("Completed tasks cannot be edited unless reverted.")
        return data
