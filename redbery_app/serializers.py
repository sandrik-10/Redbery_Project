from.models import BlogModel, Category
from rest_framework import serializers
from django.contrib.auth.models import User


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'text_color', 'background_color')

class BlogSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = BlogModel
        fields = ('id', 'title', 'description', 'image', 'published_date', 'categories', 'author', 'email')


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()

   

   
        