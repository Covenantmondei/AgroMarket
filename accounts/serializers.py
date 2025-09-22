from rest_framework import serializers
from .models import Farmer, Profile

# class UpdateProfileSerializer(serializers.Serializer):
#     first_name = serializers.CharField(max_length=30, required=False)
#     last_name = serializers.CharField(max_length=30, required=False)
#     phone_number = serializers.CharField(max_length=15, required=False)
#     address = serializers.CharField(max_length=255, required=False)
#     role = serializers.ChoiceField(choices=[('FARMER', 'Farmer'), ('BUYER', 'Buyer')], required=True)

#     def create(self, validated_data):
#         user = self.context['request'].user
#         Profile.objects.create( **validated_data)

#         profile = Profile.objects.get(user_id=user.id)

#         if validated_data.get("role") == 'FARMER' or 'Farmer':
#             Farmer.objects.create(profile=profile, **validated_data)

class UpdateProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'phone_number', 'address', 'role']

    # def create(self, validated_data):
    #     role = validated_data.get("role")
    #     if role == 'FARMER':
    #         user = self.context['request'].user
    #         profile = Profile.objects.get(user_id=user.id)
    #         Farmer.objects.create(profile=profile)

    #     return super().create(validated_data)

    def create(self, validated_data):
        create = super().create(validated_data)

        role = validated_data.get("role")

        role = role.upper()

        if role == 'FARMER':
            Farmer.objects.create(profile=create.id)


class UpdateFarmerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farmer
        fields = ['farm_name', 'farm_location']

    def create(self, validated_data):
        user = self.context['request'].user
        profile = Profile.objects.get(user_id=user.id)
        return Farmer.objects.create(profile=profile, **validated_data)