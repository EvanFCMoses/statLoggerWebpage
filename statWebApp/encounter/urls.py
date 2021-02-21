from django.contrib import admin
from django.urls import path
from encounter import views
from . import views

urlpatterns = [
        path('admin/', admin.site.urls),
	path('', views.Index.as_view(), name='index'),
]
