from rest_framework import serializers

from randoms.models import Random


class RandomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Random
        fields = '__all__'
