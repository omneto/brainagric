from django.urls import path
from . import views

urlpatterns = [
    path('', views.ApiOverview, name='home'),
    path('producers/', views.RuralProducerListApiView.as_view(), name='list-producer'),
    path('producers/<int:rural_producer_id>/', views.RuralProducerDetailApiView.as_view(), name='api-producer'),
    path('producers/list/state/', views.RuralProducerListByState.as_view(), name='list-producer-state'),
    path('producers/list/crop/', views.RuralProducerListByCrop.as_view(), name='list-producer-crop'),
    path('producers/list/area/', views.RuralProducerListByArea.as_view(), name='list-producer-area'),
]
