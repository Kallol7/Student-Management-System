from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("studentmanage.urls")),
    path("", include("myauth.urls")),
    path("", include('django_prometheus.urls'))
]
