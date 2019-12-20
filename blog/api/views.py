from rest_framework import generics
from .serializer import BlogPostSerializer
from blog.models import BlogPost
from rest_framework.permissions import IsAdminUser

class BlogListAPIView(generics.ListAPIView):
    lookup_field = 'pk'
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = (IsAdminUser,)