from django.urls import path
from . import views

urlpatterns = [
	path('display/', views.display, name='display'),
	path('update/', views.update, name='update'),
	path('query/', views.query, name='query'),
    path('show/<str:user_name>/', views.show, name='show'),
]