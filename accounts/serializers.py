from rest_framework import serializers
from .models import Farmer, Profile

class UpdateProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'phone_number', 'address', 'role']


    def create(self, validated_data):
        return super().create(validated_data)


class UpdateFarmerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farmer
        fields = ['farm_name', 'farm_location']

    def create(self, validated_data):
        user = self.context['request'].user
        profile = Profile.objects.get(user_id=user.id)
        return Farmer.objects.create(profile=profile, **validated_data)
