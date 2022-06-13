from django.contrib import admin
from django.urls import path
from .views import sign_up

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', sign_up, name="signup"),
]
