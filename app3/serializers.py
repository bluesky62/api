from rest_framework import serializers

from .models import msgModel, messagemodel


class messageSerializer(serializers.ModelSerializer):
    class Meta:
        model = messagemodel
        fields = '__all__'


class msgSerializer(serializers.ModelSerializer):
    class Meta:
        model = msgModel
        # fields = '__all__'
        fields = ['id', 'message', 'created_at', 'updated_at', 'created_by']
        depth = 1
