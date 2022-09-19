"""IR URL Configuration

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
from django.contrib import admin
from django.urls import path
from IR_HW_01.views import IR_HW_01_respond,IR_HW_01_request


urlpatterns = [
    path('admin/', admin.site.urls),
    path('IR_HW_01_respond', IR_HW_01_respond),
    path('IR_HW_01_Resquest', IR_HW_01_request),
]
