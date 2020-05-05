from rest_framework import serializers

from blog.models import Blog, BlogAuthor, BlogComment


class BlogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Blog
        fields = ['name', 'author', 'description', 'post_date']
