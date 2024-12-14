from django.urls import path
from . import views
from .webhooks import webhook

urlpatterns = [
    path('donate/', views.donate, name='donate'),
    path('donate/<int:cat_id>/', views.donate, name='donate_with_cat'),
    path('success/<str:donation_number>/', views.successMsg, name="success"),
    path('wh/', webhook, name="webhook")
]