"""nco_back URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.RegisterView.as_view()),
    path('activate/<str:code>/', user_views.ConfirmView.as_view()),
    path('login/', user_views.LoginView.as_view()),
    path('news/', user_views.NewsView.as_view()),
    path('news/<int:id>/', user_views.NewsItem.as_view()),
    path('bookmark/<int:id>/', user_views.Bookmark.as_view()),
    path('bookmark/', user_views.BookmarkUser.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
