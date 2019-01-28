from django.contrib.auth.models import User
from rest_framework import serializers
from posts.models import Post


class UserSerializer(serializers.ModelSerializer):
    posts = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Post.objects.all(), required=False)
    liked_count = serializers.SerializerMethodField()
    password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = User
        fields = (
            'id', 
            'username', 
            'email',
            'posts', 
            'liked_count', 
            'password',
            'is_active',
        )

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username'],
        )
        user.set_password(validated_data['password'])
        user.save()    
        return user

    def get_liked_count(self, obj):
        return obj.posts.filter(liked=obj).count()


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    likes = serializers.SerializerMethodField()
    
    class Meta:
        model = Post
        fields = (
            'id',
            'title',
            'content', 
            'owner', 
            'created', 
            'updated', 
            'liked', 
            'likes'
        )
    
    def get_likes(self, obj):
        return obj.liked.all().count()
