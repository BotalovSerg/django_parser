from django.urls import path

from . import views

urlpatterns = [
    path('', views.ListUsers.as_view(), name='list_user'),
    path('<int:pk>/', views.PageMessage.as_view(), name='page_m')
]
