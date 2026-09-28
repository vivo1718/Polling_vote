from django.urls import path
from . import views

urlpatterns = [
    path('', views.poll_view, name='poll_view'),
    path('vote/', views.vote_submit, name='vote_submit'),
]
