from rest_framework import serializers

from user_prefs.models import Prefs


class UserPreferencesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prefs
        fields = '__all__'

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance