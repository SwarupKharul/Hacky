"""
URL configuration for hacky project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("djoser.urls")),
    path("api/", include("djoser.urls.jwt")),
    path("api/other/", include("users.urls", namespace="users")),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("", include_docs_urls(title="API Docs")),
    path(
        "docs/",
        get_schema_view(title="API", description="API for the API", version="1.0.0"),
        name="openapi-schema",
    ),
    path(
        "hackathon/",
        include(("hackathon.urls", "hackathon"), namespace="hackathon"),
    ),
]
