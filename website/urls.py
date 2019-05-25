"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path,include

from . import views

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static 
from django.conf import settings

from blog import views as article_views

from rest_framework.urlpatterns import format_suffix_patterns



urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/',views.about,name="about"),
    path('accounts/',include('accounts.urls')),
    path('',article_views.article_list, name="article_view"),
    path('blog/',include('blog.urls')),
    path('blogg/', article_views.ArticleList.as_view()),
]
 
urlpatterns += staticfiles_urlpatterns()

urlpatterns += static(settings.MEDIA_URL,document_root= settings.MEDIA_ROOT)

urlpatterns = format_suffix_patterns(urlpatterns)