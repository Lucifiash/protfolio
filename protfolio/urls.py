"""protfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path ,include
import gallery.views
from django.conf.urls.static import static
from django.conf import settings
# import Blog.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', gallery.views.home),
    path('blog/', include("Blog.urls")),
    # path('blog/', Blog.views.blog_page),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
