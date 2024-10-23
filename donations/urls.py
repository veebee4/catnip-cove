from django.urls import path
from . import views

urlpatterns = [
    path('donate/', views.donate, name='donate'),
    path('donate/<int:cat_id>/', views.donate, name='donate_with_cat'),
    path('charge/', views.charge, name="charge"),
    path('success/<str:args>/', views.successMsg, name="success"),
]