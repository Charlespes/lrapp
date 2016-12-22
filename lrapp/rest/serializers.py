from rest_framework import serializers
from lrapp.rango.models import Category, Page
from django.contrib.auth.models import User


class CategorySerializer(serializers.ModelSerializer):
    contain_pages = serializers.HyperlinkedRelatedField(many=True, view_name='page-detail', read_only=True)
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Category
        fields = ('id', 'owner', 'name', 'likes', 'slug', 'contain_pages')


class PageSerializer(serializers.ModelSerializer):
    category = serializers.ReadOnlyField(source='category.name')
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Page
        fields = ('id', 'owner', 'title', 'likes', 'url', 'desc', 'category')


class UserSerializer(serializers.ModelSerializer):
    categories = serializers.StringRelatedField(many=True, )
    pages = serializers.StringRelatedField(many=True, )

    class Meta:
        model = User
        fields = ('id', 'username', 'categories', 'pages')
