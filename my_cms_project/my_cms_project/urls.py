"""
URL configuration for my_cms_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path,  include

# --- Configuração do Admin ---
admin.site.site_header = "Admin Panel" # O cabeçalho na página de login e no topo
admin.site.site_title = "CMS Pro - Admin" # O texto que aparece na aba do navegador
admin.site.index_title = "Welcome" # O título na página inicial do Admin
# -----------------------------

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('posts.urls')),
]
