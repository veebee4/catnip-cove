from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_cats, name='cats'),
    path('<cat_id>', views.cat_detail, name='cat_detail'),
    path('breed/<str:breed>/', views.cats_by_breed, name='cats_by_breed'),
    path('colour/<str:colour>/', views.cats_by_colour, name='cats_by_colour'),
]
