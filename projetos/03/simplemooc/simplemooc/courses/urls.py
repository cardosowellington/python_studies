from django.urls import path
from . import views

app_name = 'courses'

urlpatterns = [
  path('', views.index, name='index'),
  path('<slug:slug>/', views.details, name='details'),
  # path(r'^(?P<slug>[-\w]+)/$', views.details, name='details'),
  # path('<int:pk>/', views.details, name='details')
  # path('(?P<pk>\d+)/', views.details, name='details')
]