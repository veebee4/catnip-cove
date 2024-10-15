from django.urls import path
from . import views

urlpatterns = [
    path('donate/', views.donate, name='donate'),
    path('donate/<int:cat_id>/', views.donate, name='donate_with_cat'),
]