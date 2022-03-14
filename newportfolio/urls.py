"""newportfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
import jobs.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', jobs.views.index, name='index'),
    path('index', jobs.views.index, name='index'),
    path('admin/', admin.site.urls),
    path('lab', jobs.views.lab, name='lab'),
    path('about', jobs.views.about, name='about'),
    path('career', jobs.views.career, name='career'),
    path('contact', jobs.views.contact, name='contact'),
    path('our_work', jobs.views.our_work, name='our_work'),
    path('labentries/<int:job_id>', jobs.views.detail, name='detail'),
    path('projects/<int:project_id>',
         jobs.views.projectdetail, name='projectdetail'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
