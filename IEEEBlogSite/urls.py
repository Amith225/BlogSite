from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('blog/', include('blog.urls')),
    path('accounts/', include("accounts.urls")),
    path('accounts/', include("django.contrib.auth.urls"),)
]
