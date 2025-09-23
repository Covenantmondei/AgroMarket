from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import Profile, Farmer
from .serializers import *

class UpdateProfileView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        try:
            user, _ = Profile.objects.get_or_create(user=request.user)
            serializer = UpdateProfileSerializer(user, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"message": "Account Updated Successfully"}, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

class UpdateFarmerView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        try:
            profile = Profile.objects.get(user=request.user)
            farmer  = Farmer.objects.filter(profile=profile).first()
            if not farmer:
                return Response({"error": "Farmer profile does not exist"}, status=status.HTTP_404_NOT_FOUND)

            serializer = UpdateFarmerSerializer(farmer, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save(profile=profile)
                return Response({"message": "Farmer Profile Updated Successfully"}, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Farmer.DoesNotExist:
            return Response({"error": "Farmer profile does not exist"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        


