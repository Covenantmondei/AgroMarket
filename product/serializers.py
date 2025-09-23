from rest_framework import serializers
from .models import Product, UserCart
from accounts.models import Farmer, Profile

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ['farmer']

    def create(self, validated_data):
        user = self.context['request'].user

        farmer = Farmer.objects.filter(profile__user=user).first()
        return Product.objects.create(farmer=farmer, **validated_data)
    

class UserCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCart
        fields = '__all__'
        read_only_fields = ['buyer']

    def create(self, validated_data):
        user = self.context['request'].user

        profile = Profile.objects.get(user=user)
        product = validated_data.get('product')

        
        return UserCart.objects.create(buyer=profile, **validated_data)