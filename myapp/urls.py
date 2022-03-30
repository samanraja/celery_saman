from django.urls import path
from .views import crispyform, celerytest
from . import views


urlpatterns = [

    path('crispyform', views.crispyform, name='crispyform'),
    path('celery', views.celerytest, name='celerytest'),


]