from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('entry/<int:pk>', views.details, name='details'),
    path('entry/add', views.add, name='add'),
    path('admin/', admin.site.urls),
]
