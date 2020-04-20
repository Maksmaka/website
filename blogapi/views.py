from rest_framework.generics import get_object_or_404
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from blog.models import Blog, BlogAuthor
from .serializers import BlogSerializer


class ArticleView(ListModelMixin, CreateModelMixin, GenericAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def perform_create(self, serializer):
        author = get_object_or_404(BlogAuthor, id=self.request.data.get('author_id'))
        return serializer.save(author=author)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)