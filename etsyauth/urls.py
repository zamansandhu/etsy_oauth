from django.urls import path
from .views import *
urlpatterns = [
    path('',index,name='index'),
    path('listing',listing,name='index'),
]
