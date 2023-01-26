from django.urls import path

from . import views

urlpatterns = [
    path('', views.index_page, name='index_page'),
    path('<int:pag>/', views.page_message, name='page_m')
]
