"""portfolio URL Configuration

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
from django.urls import path

# TATE ADDED THESE
from django.conf import settings
from django.conf.urls.static import static
import jobs.views

# TATE ADDED THIS - THIS IS WHERE YOU ADD DIFFERENT PAGES LIKE HOMEPAGE ETC.
# Since the homepage contains a lot of jobs it makes since that we would add the homepage to the jobs --> views.py  # noqa
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', jobs.views.home, name='home'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
