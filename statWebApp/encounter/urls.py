from django.contrib import admin
from django.urls import path, include
from encounter import views
from . import views

urlpatterns = [
        path('admin/', admin.site.urls),
        path('login/', views.loginDataEntry, name='loginDataEntry'),
	path('', views.dataEntry, name='dataEntry'),
]
