"""
URL configuration for hello_world project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from hello_world.core import views as core_views
from mythical_app import views as mythical_views

urlpatterns = [
    path("", core_views.index),
    path("patients/", mythical_views.patient_list, name="patient_list"),
    path("owners/", mythical_views.OwnerListView.as_view(), name="owner_list"),
    path("owners/new/", mythical_views.OwnerCreateView.as_view(), name="owner_create"),
    path("owners/<int:pk>/edit/", mythical_views.OwnerUpdateView.as_view(), name="owner_update"),
    path("owners/<int:pk>/delete/", mythical_views.OwnerDeleteView.as_view(), name="owner_delete"),
    path("admin/", admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
