from django.contrib import admin
from django.urls import path, include
from teams.views import index, read_rules, subscribe

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('rules/', read_rules, name='rules'),
    path('subscribe/', subscribe, name='subscribe'),

]
