"""catalyst_count URL Configuration

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
from django.conf.urls import url
from catalyst import views
 
urlpatterns = [ 
    url(r'^api/v1/home$', views.home),
    url(r'^api/v1/catalyst-count$', views.retrieve_companies),
    url(r'^api/v1/catalyst-count/(?P<id>[0-9]+)$', views.retrieve_company),
    url(r'^api/v1/catalyst-count/upload$', views.add_company),
    url(r'^api/v1/users$', views.retrieve_users),
    url(r'^api/v1/(?P<id>[0-9]+)$', views.retrieve_user),
    url(r'^api/v1/users/upload$', views.add_user),
]
