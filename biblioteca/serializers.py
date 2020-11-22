"""
Biblioteca Serializers
"""

from rest_framework.serializers import ModelSerializer
from biblioteca.models import Author, Publisher, Book


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
