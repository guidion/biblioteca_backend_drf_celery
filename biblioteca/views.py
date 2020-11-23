from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from biblioteca.serializers import UserSerializer, AuthorSerializer, PublisherSerializer, BookSerializer


class UserList(ListCreateAPIView):
    serializer_class = UserSerializer
    model = serializer_class.Meta.model
    queryset = model.objects.all()
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]


class UserDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    model = serializer_class.Meta.model
    queryset = model.objects.all()
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]


class AuthorList(ListCreateAPIView):
    serializer_class = AuthorSerializer
    model = serializer_class.Meta.model
    queryset = model.objects.all()
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]


class AuthorDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = AuthorSerializer
    model = serializer_class.Meta.model
    queryset = model.objects.all()
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]


class PublisherList(ListCreateAPIView):
    serializer_class = PublisherSerializer
    model = serializer_class.Meta.model
    queryset = model.objects.all()
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]


class PublisherDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = PublisherSerializer
    model = serializer_class.Meta.model
    queryset = model.objects.all()
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]


class BookList(ListCreateAPIView):
    serializer_class = BookSerializer
    model = serializer_class.Meta.model
    queryset = model.objects.all()
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [JWTAuthentication]


class BookDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = BookSerializer
    model = serializer_class.Meta.model
    queryset = model.objects.all()
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [JWTAuthentication]
