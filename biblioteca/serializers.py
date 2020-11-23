"""
Biblioteca Serializers
"""
from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer
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
            'password': {'write_only': True}
        }


class CustomSerializer(ModelSerializer):
    """
    Custom Serializer
    """
    def create(self, validated_data):
        """
        Create and return a new Models instance, given the validated data
        """
        # Create main Object
        main_object = self.__class__.Meta.model.objects.create(**validated_data)  # pylint: disable=no-member
        # Return object created
        return main_object


class AuthorSerializer(CustomSerializer):
    """
    Author serializer
    """

    class Meta:  # pylint: disable=too-few-public-methods
        """
        Serializer Class Meta
        """
        model = Author
        fields = '__all__'


class PublisherSerializer(CustomSerializer):
    """
    Publisher serializer
    """

    class Meta:  # pylint: disable=too-few-public-methods
        """
        Serializer Class Meta
        """
        model = Publisher
        fields = '__all__'


class BookSerializer(CustomSerializer):
    """
    Book serializer
    """

    class Meta:  # pylint: disable=too-few-public-methods
        """
        Serializer Class Meta
        """
        model = Book
        fields = '__all__'
