from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response

from blog.models import Blog
from .serializers import BlogSerializer


# class BlogView(viewsets.ViewSet):
#     """
#     A simple ViewSet that for listing or retrieving users.
#     """
#     def list(self, request):
#         queryset = Blog.objects.all()
#         serializer = BlogSerializer(queryset, many=True)
#         return Response(serializer.data)
#
#     def retrieve(self, request, pk=None):
#         queryset = Blog.objects.all()
#         user = get_object_or_404(queryset, pk=pk)
#         serializer = BlogSerializer(user)
#         return Response(serializer.data)


class BlogViewSet(viewsets.ModelViewSet):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()
