from rest_framework import status
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.response import Response
from posts.models import Post
from posts.api.serializers import PostSerializer

# Forma más sencilla de crear un CRUD completo


class PostModelViewSet(ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


# class PostViewSet(ViewSet):
#     def list(self, request):
#         serializer = PostSerializer(Post.objects.all(), many=True)
#         return Response(status=status.HTTP_200_OK, data=serializer.data)

#     def retrieve(self, request, pk=None):
#         post = PostSerializer(Post.objects.get(pk=pk))
#         return Response(status=status.HTTP_200_OK, data=post.data)

#     def create(self, request):
#         serializer = PostSerializer(data=request.POST)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(status=status.HTTP_201_CREATED, data=serializer.data)
#         return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)


# class PostApiView(APIView):
#     def get(self, request):
#         # posts = [post.title for post in Post.objects.all()]
#         serializer = PostSerializer(Post.objects.all(), many=True)
#         return Response(status=status.HTTP_200_OK, data=serializer.data)

#     def post(self, request):
#         serializer = PostSerializer(data=request.POST)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(status=status.HTTP_201_CREATED, data=serializer.data)
#         return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)
