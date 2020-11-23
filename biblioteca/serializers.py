"""
Biblioteca Serializers
"""
from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer, ListField, IntegerField, CharField
from biblioteca.models import Author, Publisher, Book


class UserSerializer(ModelSerializer):

    def create(self, validated_data):
        user_model = get_user_model()
        user = user_model.objects.create_user(**validated_data)
        return user

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)
        return super(UserSerializer, self).update(instance, validated_data)

    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name')
        extra_kwargs = {
            'password': {'write_only': True},
            'first_name': {'required': True},
            'last_name': {'required': True},
            'email': {'required': True},
        }


class AuthorSerializer(ModelSerializer):
    """
    Author serializer
    """

    class Meta:  # pylint: disable=too-few-public-methods
        """
        Serializer Class Meta
        """
        model = Author
        fields = '__all__'


class AuthorRelatedSerializer(ModelSerializer):
    """
    Author serializer
    """

    class Meta:  # pylint: disable=too-few-public-methods
        """
        Serializer Class Meta
        """
        model = Author
        fields = ('id', )


class PublisherSerializer(ModelSerializer):
    """
    Publisher serializer
    """

    class Meta:  # pylint: disable=too-few-public-methods
        """
        Serializer Class Meta
        """
        model = Publisher
        fields = '__all__'


class BookSerializer(ModelSerializer):
    """
    Book serializer
    """
    authors = AuthorSerializer(read_only=True, many=True)
    authors_registry = CharField(write_only=True)

    class Meta:  # pylint: disable=too-few-public-methods
        """
        Serializer Class Meta
        """
        model = Book
        fields = '__all__'

    def create(self, validated_data):
        """
        Create and return a new Models instance, given the validated data
        """
        # Create main Object
        authors_registry = validated_data.pop('authors_registry')
        authors_registry = [int(author_registry) for author_registry in authors_registry.split(',')]
        _authors = Author.objects.filter(pk__in=authors_registry)
        if _authors:
            book = Book(**validated_data)
            book.save()
            for author in _authors:
                print('Author: ', author)
                book.authors.add(author)
            book.save()
        return book

    def update(self, instance, validated_data):
        """
        Update and return a instance, given the validated data
        """
        authors_registry = validated_data.pop('authors_registry')
        authors_registry = [int(author_registry) for author_registry in authors_registry.split(',')]
        _authors = Author.objects.filter(pk__in=authors_registry)
        if _authors:
            pk = instance.id
            instance.delete()
            instance = Book(**validated_data, id=pk)
            instance.save()
            for author in _authors:
                print('Author: ', author)
                instance.authors.add(author)
            instance.save()
        return instance
