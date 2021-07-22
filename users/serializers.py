from datetime import datetime

from django.contrib import auth
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from main.models import News, Bookmarks
from users.models import ConfirmationCode


class UserCreateSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=100)

    def validate_email(selfe, email):
        if User.objects.filter(username=email):
            raise ValidationError("Такой пользователь уже существует!")
        return email


class ConfirmCodeSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=100, min_length=16)

    def validate_code(self, code):
        codes = ConfirmationCode.objects.filter(code=code)
        if not codes:
            raise ValidationError("Такого кода нет!")
        elif codes.filter(valid_until__lt=datetime.now()):
            raise ValidationError("Истек срок действия активации")
        return code


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ("id", "title", "short_description", "description", "created", "link", "image")

    def to_representation(self, instance):
        data = super().to_representation(instance)
        bool = Bookmarks.objects.filter(news=instance).first()
        if bool:
            data["bool"] = bool.book
        else:
            data['bool'] = False
        return data

class BookmarkSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bookmarks
        fields = ('id', 'user', 'book')

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['news'] = NewsSerializer(instance.news).data
        return data
