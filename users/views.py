import secrets
from datetime import datetime, timedelta

from django.conf import settings
from django.contrib import auth
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import render

# Create your views here.
from rest_framework.authtoken.models import Token
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import mixins, viewsets, status
from main.models import News, Bookmarks
from users.models import ConfirmationCode
from users.serializers import UserCreateSerializer, ConfirmCodeSerializer, NewsSerializer, BookmarkSerializer


class RegisterView(APIView):
    def post(self, request):
        serializer = UserCreateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                data={
                    'message': 'ERROR',
                    'error': serializer.errors
                }
            )
        email = request.data.get('email')
        password = request.data.get('password')
        user = User.objects.create_user(
            username=email,
            email=email,
            password=password,
            is_active=False
        )
        code = secrets.token_urlsafe(16)
        confirmation_code = ConfirmationCode.objects.create(
            user=user,
            code=code,
            valid_until=datetime.now() + timedelta(minutes=5)
        )
        send_mail(
            subject='Activation code',
            message=f'{request.META["HTTP_HOST"]}/activate/{code}/',
            from_email=settings.EMAIL_HOST,
            recipient_list=[email]
        )
        Token.objects.create(user=user)

        return Response(data={'message': 'OK'})


class ConfirmView(APIView):
    def get(self, request, code):
        serializer = ConfirmCodeSerializer(data={'code': code})
        if not serializer.is_valid():
            return Response(
                data={
                    'errors': serializer.errors
                }
            )
        codes = ConfirmationCode.objects.filter(code=code)
        if codes:
            user = codes[0].user
            user.is_active = True
            user.save()
        return Response(data={'massage': 'ok'})


class LoginView(APIView):

    def post(self, request):
        email = request.data['email']
        password = request.data['password']
        user = auth.authenticate(username=email, password=password)
        if user:
            tokens = Token.objects.filter(user=user).first()
            tokens.delete()
            token = Token.objects.create(user=user)
            auth.login(request=request, user=user)
            return Response(data={'token': f"{token.key}"})
        else:
            Response(data={"errors": "такого юзера нет"})


class NewsView(ListAPIView):
    serializer_class = NewsSerializer
    queryset = News.objects.all()


class NewsItem(RetrieveAPIView):
    serializer_class = NewsSerializer
    queryset = News.objects.filter()
    lookup_field = "id"


class Bookmark(CreateAPIView):

    def create(self, request, *args, **kwargs):
        news = get_object_or_404(News, pk=kwargs["id"])
        print(news)
        Bookmarks.objects.create(book=True, news=news, user=request.user)
        return Response(status=status.HTTP_201_CREATED)


class BookmarkUser(ListAPIView):
    serializer_class = BookmarkSerializer

    def get_queryset(self):
        return Bookmarks.objects.filter(user=self.request.user)
