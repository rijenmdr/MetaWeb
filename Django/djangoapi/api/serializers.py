from rest_framework import serializers
from .models import Member, Website, Owner


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ['id', 'name', 'added_by', 'created_date']


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member      
        fields = ['id', 'title', 'description']


class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = ['id', 'username', 'email', 'phone']


class WebsiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Website
        fields = ['id', 'title', 'description', 'user', 'menus']
