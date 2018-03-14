"""Beta4 URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from oficio import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('oficio/', views.oficio),
    path('detalhes/<int:oficio_id>/', views.detalhes),
    path('delete/<int:numero>/', views.delete),
    path('visualizar/<int:oficio_id>/', views.visualizar),
    path('novo/', views.novo),
    path('', views.home),
    path('detalhes/<int:oficio_id>/pdf/', views.render_pdf_view),
    path('login/',views.do_login),
    path('logout/',views.do_logout),
]   + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)