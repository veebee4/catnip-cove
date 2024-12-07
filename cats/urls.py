from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_cats, name='cats'),
    path('<int:cat_id>/', views.cat_detail, name='cat_detail'),
    path('breed/<str:breed>/', views.cats_by_breed, name='cats_by_breed'),
    path('colour/<str:colour>/', views.cats_by_colour, name='cats_by_colour'),
    path('add/', views.add_cat, name='add_cat'),
    path('edit/<int:cat_id>/', views.edit_cat, name='edit_cat'),
    path('delete/<int:cat_id>/', views.delete_cat, name='delete_cat'),
]
