from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('polls/', views.poll_list, name='poll_list'),
    path('polls/<int:poll_id>/', views.poll_detail, name='poll_detail'),
    path('candidates/', views.candidate_list, name='candidate_list'),
    path('candidates/<int:candidate_id>/', views.candidate_detail, name='candidate_detail'),
    path('party_detail/<int:id>', views.party_detail, name='party_detail'),
    path('party_list/', views.party_list, name='party_list'),
]
