"""cv_fr URL Configuration

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
from django.urls import path

#main페이지 수정하기 위함
#from . import views #.(현재경로에있는) views 파일을 import하라
#import profiles.views


#profile 데이터베이스의 image를 띄우기 위함
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    #views라는 파일이 있음을 알아야함으로 import해줘야한다.
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
