from django.urls import path

from similarity import views

urlpatterns = [
    path('', views.TextView.as_view(), name='home'),
]