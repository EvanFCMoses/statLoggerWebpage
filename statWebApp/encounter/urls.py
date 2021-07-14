from django.contrib import admin
from django.urls import path
from encounter import views
from . import views

urlpatterns = [
        path('admin/', admin.site.urls),
        # path('process/', views.process, name='process'),
	path('', views.DataEntry.as_view(), name='dataEntry'),
]
