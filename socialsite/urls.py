"""socialsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from jet.dashboard.dashboard_modules import google_analytics_views
from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include
from socialsite.views import HomePage, Test, Thanks

urlpatterns = [
    path('',HomePage.as_view(),name='home'),
    path('test/',Test.as_view(),name='test'),
    path('thanks/',Thanks.as_view(),name='thanks'),
    path('accounts/',include('accounts.urls')),
    path('groups/',include('groups.urls',namespace='groups')),
    path('posts/',include('posts.urls',namespace='posts')),
    path('accounts/',include('django.contrib.auth.urls')),
    url(r'^jet/', include('jet.urls', 'jet')),
    url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    path('admin/', admin.site.urls),
]
