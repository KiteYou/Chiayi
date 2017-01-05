from django.conf.urls import url
from travel import views

urlpatterns = [
    url(r'^$', views.travel, name='travel'),
]